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
    

