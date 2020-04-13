from flask import Blueprint, render_template,request, redirect, flash
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user
from models.user import User 

sessions_blueprint = Blueprint("sessions", __name__, template_folder="templates")

@sessions_blueprint.route("/login")
def new():
    return render_template("sessions/new.html")

@sessions_blueprint.route("/login", methods=["POST"])
def create():
    email = request.form.get("email")
    password = request.form.get("password")
    user = User.get_or_none(User.email == email)
    if user and check_password_hash(user.password, password):
        login_user(user)
        return redirect("/")
    else:
        flash("Invalid credentials")
        return redirect("/login")

@sessions_blueprint.route("/logout", methods=["POST"])
def destroy():
    logout_user()
    return redirect("/")

# @sessions_blueprint.route("/profileimage")
# def ():
#     return render_template("sessions/uploadimage.html")