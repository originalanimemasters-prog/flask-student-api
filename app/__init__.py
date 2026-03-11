
from flask import Flask
from .extensions import db, jwt
from .blueprints.auth import auth_bp
from .blueprints.students import student_bp
from .utils.blacklist import token_in_blocklist_loader
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")

    db.init_app(app)
    jwt.init_app(app)

    jwt.token_in_blocklist_loader(token_in_blocklist_loader)

    app.register_blueprint(auth_bp)
    app.register_blueprint(student_bp)

    with app.app_context():
        db.create_all()

    return app
