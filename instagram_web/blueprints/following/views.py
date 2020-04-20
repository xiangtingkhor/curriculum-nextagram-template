from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user
from models.following import Following
from models.user import User

following_blueprint = Blueprint('following',
                             __name__,
                             template_folder='templates')

@following_blueprint.route('/<id>', methods = ["POST"])
def follow(id):
    # idol_id = request.form.get('profile_user_id')
    idol_id = id
    print(f"idol id : {idol_id}")
    follower_id = current_user.id
    print(f"follower id : {follower_id}")
    following_record = Following(idol = int(idol_id), follower = follower_id)
    following_record.save()
    # Following.create(idol = idol_id, follower = follower_id, approved = False)
    print("successfully created a record")
    print(User.get(User.id == idol_id).name)
    return redirect(url_for('users.show', username = User.get(User.id == idol_id).name))#user stays at idol's profile page

@following_blueprint.route('/approve/<id>', methods = ["POST"])
def approve(id):
    approval_user = Following.get((Following.follower_id == id) & (Following.idol_id == current_user.id))
    approval_user.approved = True
    approval_user.save()
    return redirect(url_for('users.show', username = current_user.name))#user stays at his profile page