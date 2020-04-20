from flask import Blueprint
from flask import jsonify

users_api_blueprint = Blueprint('users_api',
                             __name__,
                             template_folder='templates')

@users_api_blueprint.route('/', methods=['GET'])
def get_current_user():
    return jsonify(username=g.user.username,
                    email = g.user.email,
                    id = g.user.id)

# from flask import Blueprint, jsonify, request, flash, redirect, url_for
# from models.user import User
# from flask_login import current_user
# from flask_jwt_extended import (jwt_required, create_access_token, get_jwt_identity)
# from app import csrf
# from werkzeug.security import check_password_hash
# from flask_login import login_user
# from instagram_web.util.upload_imgs import upload
# from models.images import Images


# users_api_blueprint = Blueprint('users_api',
#                              __name__,
#                              template_folder='templates')

# @users_api_blueprint.route('/', methods=['GET'])
# def users():
#     users = User.select()
#     return jsonify([{"username": user.name, "id": user.id, "email": user.email, "profileImage": user.profile_img_url} for user in users])

# @users_api_blueprint.route('/images/userId=<id>', methods=['GET'])
# def images(id):
#     user = User.get_by_id(id)
#     print(user)
#     return jsonify([{"id": image.id, "url": image.img_url} for image in user.images])

# @users_api_blueprint.route('/<id>', methods=['GET'])
# def users_id(id):
#     user = User.get_by_id(id) 
#     print(user)
#     print(user.images)
#     return jsonify({"username": user.name, "id": user.id, "profileImage": user.profile_img_url})

# @users_api_blueprint.route('/images/me', methods=['GET'])
# @jwt_required
# def users_images():
#     user = User.get_by_id(get_jwt_identity())
#     # return jsonify({"src":user.images[0].img_url})
#     return jsonify([img.img_url for img in user.images])

# @users_api_blueprint.route('/login', methods=['POST'])
# @csrf.exempt
# def login_check():
#     login = request.get_json()
#     print(login)
#     user = User.get_or_none(User.name == login['username'])
#     print(user)

#     if user:#return true if the email is available inside our database
#         print(login['password'])
#         password_to_check = login['password']
#         hashed_password = user.password
#         result = check_password_hash(hashed_password, password_to_check)
#         print(result)
#         if result:
#             access_token = create_access_token(identity=user.id)

#             # flash(f"Login successful.")
#             # session["email"] = request.form['email_input']
#             # flash(f"{session['email']}")
#             return jsonify({"auth_token": access_token, "message": "Successfully login", "status": "Success", "user":{"id":user.id, "username": user.name, "email": user.email}})
    

#     return jsonify({"message": "Some error occur", "status":"failed"})

# @users_api_blueprint.route('/me', methods=['GET'])
# @jwt_required
# def my_info():
#     user = User.get_by_id(get_jwt_identity())
#     print(get_jwt_identity())
#     return jsonify({"id": user.id, "email":user.email, "profile_picture": user.profile_img_url, "username": user.name})

# @users_api_blueprint.route('/', methods=['POST'])
# @csrf.exempt
# def sign_up():
#     sign_up_data = request.get_json()
#     print(sign_up_data)
#     username_input = sign_up_data['username']
#     password_input = sign_up_data['password']
#     email_input = sign_up_data['email']
#     username_check = User.get_or_none(User.name == username_input)
#     email_check = User.get_or_none(User.email == email_input)
#     user = User(name = username_input, password = password_input, email = email_input)

#     if username_input == "" or password_input == "" or email_input == "":
#         return jsonify({"message": "All fields are required", "status": "failed"})

#     elif username_check :
#         return jsonify({"message":["username is in use"], "status":"failed"})

#     elif user.save():
#         access_token = create_access_token(identity=username_input)
#         # print(access_token)
    
#         registered_user = User.get(User.name == username_input)
#         print(registered_user)
#         return jsonify({"auth_token": access_token, "message": "Successfully created a user and signed in.", "status": "Success", "user":{"id": registered_user.id, "username": registered_user.name, "profile_picture":registered_user.profile_img_url}})
        
#     else:
#         return jsonify({"message": "Some error happened", "status": "Failed"})

# @users_api_blueprint.route('/check_name/username=<username>', methods=['GET'])
# def check_name(username):
#     username_check = User.get_or_none(User.name == username)
#     if username_check:
#         exist_status = True
#         valid_status = False
#     else:
#         exist_status = False
#         valid_status = True

#     return jsonify({"exists":exist_status, "valid":valid_status})

# @users_api_blueprint.route('/upload_images', methods=['POST'])
# @jwt_required
# @csrf.exempt
# def upload_img():
#     from app import app

#     file = request.files.get("image")
#     print(f"upload images:{file}")
#     result = upload(file)
#     print(get_jwt_identity())
#     image = Images(user = get_jwt_identity(), img = result)
#     image.save()

#     return jsonify({"images_url":"app.config.get('AWS_S3_DOMAIN')"+file.filename, "success":True})
    

