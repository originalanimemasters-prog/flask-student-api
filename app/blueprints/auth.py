
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from ..extensions import db
from ..models.user import User
from ..utils.blacklist import add_token_to_blocklist
from ..utils.rate_limit import rate_limit

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
@rate_limit(10, 60)
def register():
    data = request.get_json()

    if not data or "username" not in data or "password" not in data or "role" not in data:
        return jsonify({"error": "username, password and role required"}), 400

    if data["role"] not in ["admin", "student"]:
        return jsonify({"error": "Role must be admin or student"}), 400

    if len(data["password"]) < 6:
        return jsonify({"error": "Password must be at least 6 characters"}), 400

    if User.query.filter_by(username=data["username"]).first():
        return jsonify({"error": "Username already exists"}), 400

    hashed = generate_password_hash(data["password"])

    user = User(username=data["username"], password=hashed, role=data["role"])
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered"}), 201


@auth_bp.route("/login", methods=["POST"])
@rate_limit(10, 60)
def login():
    data = request.get_json()

    user = User.query.filter_by(username=data.get("username")).first()

    if not user or not check_password_hash(user.password, data.get("password")):
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_access_token(
        identity=user.username,
        additional_claims={"role": user.role}
    )

    return jsonify({"access_token": token})


@auth_bp.route("/logout", methods=["POST"])
@jwt_required()
def logout():
    jwt_data = get_jwt()
    add_token_to_blocklist(jwt_data["jti"])
    return jsonify({"message": "Logged out"})
