#!/usr/bin/python3
"""Start a Flask Application."""
from os import getenv
from flask import Flask, render_template, request, jsonify, redirect, url_for, make_response
from datetime import datetime
from uuid import uuid4
from models.storage import Storage
from models.learner import Learner
from models.trainer import Trainer
from models.admin import Admin
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from flask_jwt_extended import JWTManager, create_access_token, jwt_required


app = Flask(__name__)
app.config["SECRET_KEY"] = getenv("FLASK_SECRET_KEY")
JWTManager(app)

storage = Storage()

SUB_DOMAIN = "/gcf"


@app.errorhandler(404)
def not_found(error):
    """Handle view for page not found"""
    return render_template("not_found.html")


@app.route(f"{SUB_DOMAIN}/home", strict_slashes=False)
def home():
    """Handle the home view."""
    return render_template("home.html", cache_id=uuid4())


@app.route(
        f"{SUB_DOMAIN}/admin-login",
        methods=["GET", "POST"],
        strict_slashes=False
)
def admin():
    """Handle Admin-login view"""
    if request.method == "GET":
        return render_template("admin.html", cache_id=uuid4())

    data = request.form
    username = data.get("username")
    passkey = data.get("passkey")
    session = storage.get_session()

    user = session.query(Admin).filter_by(username=username).first()
    if user:
        access_token = create_access_token(identity=user.id)
        response = make_response(redirect(url_for('admin_dashboard')))
        response.set_cookie("access_token_cookie", access_token, httponly=True, secure=True)
        return response
    return jsonify({"msg": "Invalid Username or Passkey"})


@app.route(f"{SUB_DOMAIN}/admin-dashboard")
@jwt_required(locations=["cookies"])
def admin_dashboard():
    """Handles view for admin dashboard."""
    return render_template("admin_dashboard.html")


@app.route(f"{SUB_DOMAIN}/trainers")
@jwt_required(locations=["cookies"])
def get_trainers():
    """Retrieve all trainers from the database."""
    try:
        trainers = storage.all(Trainer).values()
        sorted_trainers = sorted(trainers, key=lambda trainer: trainer.create_at)

        sorted_trainers_list = [
            {
                "name": trainer.name,
                "email": trainer.email,
                "contact": trainer.phone_number,
                "create_at": trainer.create_at,
                "skills": trainer.skills
            } for trainer in sorted_trainers
        ]
        return jsonify(sorted_trainers_list)
    except SQLAlchemyError as e:
        storage.session.rollback()  # Rollback in case of error
        print(str(e))
        return jsonify({"error": str(e)}), 500
    finally:
        storage.close()


@app.route(f"{SUB_DOMAIN}/learners")
def get_learners():
    """Retrieve all learners from the database."""
    try:
        learners = storage.all(Learner).values()
        sorted_learners = sorted(learners, key=lambda learner: learner.create_at)

        sorted_learners_list = [
            {
                "name": learner.name,
                "email": learner.email,
                "contact": learner.phone_number,
                "create_at": learner.create_at,
                "skills": ", ".join(learner.skills),
                "other_skills": learner.other_skills
            } for learner in sorted_learners
        ]
        return jsonify(sorted_learners_list)
    except SQLAlchemyError as e:
        storage.session.rollback()
        print(str(e))
        return jsonify({"error": str(e)}), 500
    finally:
        storage.close()


@app.route(f"{SUB_DOMAIN}/register-learner", methods=["POST", "GET"])
def register_learner():
    """Handle view for registration."""
    if request.method == "GET":
        return render_template("learner.html", cache_id=uuid4())

    data = request.get_json()
    attr = {
            "name": data.get("name"),
            "email": data.get("email"),
            "other_skills": data.get("other_skills"),
            "phone_number": data.get("phone_number"),
            "skills": data.get("skills")
            }
    if registration(attr, Learner):
        return jsonify({
            "status": "Success",
            "msg": "Registration Successful"
            }), 201
    else:
        return jsonify({"msg": "User Already Exists"}), 422


@app.route(f"{SUB_DOMAIN}/register-trainer", methods=["POST", "GET"])
def register_trainer():
    """Handle view for volunteer trainer registration."""
    if request.method == "GET":
        return render_template("trainer.html", cache_id=uuid4())

    data = request.get_json()
    attr = {"name": data.get("name"), "email": data.get("email"),
            "phone_number": data.get("phone_number"), "skills": data.get("skills")}
    if registration(attr, Trainer):
        return jsonify({
            "status": "Success",
            "msg": "Registration Successful"
            }), 201
    else:
        return jsonify({"msg": "User Already Exists"}), 422


@app.route(f"{SUB_DOMAIN}/register-success")
def register_success():
    """Handle view for registration success for trainer and learner."""
    return render_template("registration_success.html")


@app.route(f"{SUB_DOMAIN}/register-fail")
def register_fail():
    """Handle view for failed registration."""
    return render_template("registration_failure.html")


#-------------------------FunctionDefinition----------------------#
def registration(attr, cls):
    """Save and instance to database.
    Args:
        attr (dict): The key/value pair of attribute.
        cls (Class): Class name to create an instance.
    """

    learner = cls(**attr)
    try:
        storage.new(learner)
        storage.save()
        return True
    except IntegrityError:
        storage.rollback()
        return False
    finally:
        storage.close()


if __name__ == "__main__":
    app.run(debug=True, port=5000)
