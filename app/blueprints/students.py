
from flask import Blueprint, request, jsonify
from ..extensions import db
from ..models.student import Student
from ..utils.decorators import role_required

student_bp = Blueprint("students", __name__)

@student_bp.route("/students", methods=["GET"])
def get_students():
    page = request.args.get("page", 1, type=int)
    limit = request.args.get("limit", 10, type=int)

    pagination = Student.query.paginate(page=page, per_page=limit, error_out=False)

    return jsonify({
        "students": [s.to_dict() for s in pagination.items],
        "page": page,
        "pages": pagination.pages
    })

@student_bp.route("/students", methods=["POST"])
@role_required("admin")
def add_student():
    data = request.get_json()

    if "name" not in data or "age" not in data:
        return jsonify({"error": "name and age required"}), 400

    student = Student(name=data["name"], age=data["age"])
    db.session.add(student)
    db.session.commit()

    return jsonify(student.to_dict()), 201

@student_bp.route("/students/<int:student_id>", methods=["PATCH"])
@role_required("admin")
def update_student(student_id):
    student = db.session.get(Student, student_id)

    if not student:
        return jsonify({"error": "Student not found"}), 404

    data = request.get_json()

    if "name" in data:
        student.name = data["name"]

    if "age" in data:
        student.age = data["age"]

    db.session.commit()

    return jsonify(student.to_dict())

@student_bp.route("/students/<int:student_id>", methods=["DELETE"])
@role_required("admin")
def delete_student(student_id):
    student = db.session.get(Student, student_id)

    if not student:
        return jsonify({"error": "Student not found"}), 404

    db.session.delete(student)
    db.session.commit()

    return jsonify({"message": "Deleted"})
