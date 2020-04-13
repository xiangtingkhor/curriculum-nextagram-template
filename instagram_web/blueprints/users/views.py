from flask import Blueprint, render_template, url_for, redirect, request, abort
from models.user import User
from flask_login import login_required
from flask_wtf.csrf import CSRFProtect

users_blueprint = Blueprint('users',
                            __name__,
                            template_folder='templates')


@users_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('users/new.html')

@users_blueprint.route('/', methods=['POST'])
def create():
    user = User.create(username=request.form["username"],
    email=request.form.get["email"],
    name=request.form.get["name"],
    password=request.form.get["password"])

    if len(user.errors) > 0 :
        return render_template("users/new.html", errors = user.errors)
    else:
        return redirect(url_for("home"))

@users_blueprint.route('/<id>', methods=["GET"])
@login_required
def show(id):
    user = User.get_by_id(id)
    if current_user.id == user.id:
        return render_template('users/show.html', user = user)
    else:
        abort(404)



@users_blueprint.route('/', methods=["GET"])
def index():
    return "USERS"


@users_blueprint.route('/<id>/edit', methods=['GET'])
def edit(id):
    pass


@users_blueprint.route('/<id>', methods=['POST'])
def update(id):
    pass
