from flask import Blueprint, render_template, request, redirect, url_for
from models.images import Images
from flask_login import current_user
from instagram_web.util.upload_imgs import upload

images_blueprint = Blueprint('images',
                             __name__,
                             template_folder='templates')

@images_blueprint.route('/')
def index():
    return render_template('images/new.html')

@images_blueprint.route('/receive-upload-images', methods = ["POST"])
def create():
    file = request.files.get('upload_images')
    print(file)
    print(file.filename)
    result = upload(file)
    print(result)
    Images.create(user = current_user.id, img = result)

    return redirect(url_for('users.show', username = current_user.name))
