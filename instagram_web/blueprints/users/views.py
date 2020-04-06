from flask import Blueprint, render_template, url_for, redirect, request
from models.user import User

users_blueprint = Blueprint('users',
                            __name__,
                            template_folder='templates')


@users_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('users/new.html')

@users_blueprint.route('/', methods=['POST'])
def create():
    user = User.create(username=request.form["username"],
    email=request.form["email"],
    name=request.form["name"],
    password=request.form["password"])

    if len(user.errors) > 0 :
        return render_template("users/new.html", errors = user.errors)
    else:
        return redirect(url_for("home"))

@users_blueprint.route('/<username>', methods=["GET"])
def show(username):
    pass


@users_blueprint.route('/', methods=["GET"])
def index():
    return "USERS"


@users_blueprint.route('/<id>/edit', methods=['GET'])
def edit(id):
    pass


@users_blueprint.route('/<id>', methods=['POST'])
def update(id):
    pass
