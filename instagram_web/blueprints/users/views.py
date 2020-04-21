from flask import Flask, Blueprint, render_template, request, flash, redirect, url_for, abort
from models.user import User
from models.donation import Donation
from flask_login import current_user, login_user, login_required
from instagram_web.util.upload_imgs import upload
from models.images import Images
import braintree
import os
from decimal import Decimal
from instagram_web.util.email import send_message

gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        braintree.Environment.Sandbox,
        merchant_id=os.environ.get('MERCHANT_ID'),
        public_key=os.environ.get('PUBLIC_KEY'),
        private_key=os.environ.get('PRIVATE_KEY')
    )
)

users_blueprint = Blueprint('users',
                            __name__,
                            template_folder='templates')
@users_blueprint.route('/')
def index():
    
    return render_template('home.html')

@users_blueprint.route('/new', methods=['GET'])
def new():
    if not current_user.is_authenticated:

        return render_template('users/new.html')
    else:
        return redirect(url_for('users.index'))

@users_blueprint.route('/receive-sign-up', methods=['POST'])
def create():
    username_input = request.form.get('username_input')
    password_input = request.form.get('password_input')
    email_input = request.form.get('email_input')
    user = User(name = username_input, password = password_input, email = email_input)
    if user.save():
        flash(f"Account has been created successful")
        login_user(user)
        return redirect(url_for('users.index'))
        
    else:
        return render_template('users/new.html', errors = user.errors)
 

@users_blueprint.route('/<username>', methods=["GET"])
@login_required
def show(username):
    user = User.get(User.name == username)
    client_token = gateway.client_token.generate()
    
    return render_template('users/user_profile.html', user = user, client_token = client_token)


@users_blueprint.route('/<id>/edit', methods = ["POST"])
@login_required
def edit(id):
    update_type = request.form.get("update_type")
    print(update_type)
    print(request.form.get("update_type"))
    if update_type == "update_name":
        return render_template('users/edit_profile.html')
    elif update_type == "update_profile_image":
        return render_template('users/upload_image.html')

    
@users_blueprint.route('/<id>', methods=['POST'])
@login_required

def update(id):
    user = User.get_by_id(id)
    update_type = request.form.get("update_type")
    client_token = gateway.client_token.generate()
    print(update_type)
    print(user)
    if current_user == user:
        if update_type == "update_name":
            User.update(name = request.form.get('edit_profile_name')).where(User.id == id).execute()
            return redirect(url_for('users.show', username = request.form.get('edit_profile_name')))
            
        elif update_type == "update_profile_image":
            print('inside update profile image')
            file = request.files.get('upload_profile_img')
            print(file)
            print(file.filename)
            result = upload(file)
            print(result)
            user.profile_img = result
            print(user.profile_img)
            user.save()
            print(user.errors)
            print(current_user.profile_img)
            print('it is updated')
            return redirect(url_for('users.show', username = user.name))
            

        else:
            flash("unable to update, something is wrong.")
            return redirect(url_for('users.show', username = current_user.name))
    
    else:
        return redirect(url_for('users.index'))

@users_blueprint.route("/checkout", methods=["POST"])
def checkout():
    print(request.form.get('paymentMethodNonce'))
    donation_amount = request.form.get('donation_amount')
    Donation.create(user = current_user.id, amount = donation_amount)
    print(donation_amount)
    result = gateway.transaction.sale({
    "amount": donation_amount,
    "payment_method_nonce": request.form.get('paymentMethodNonce'),
    "options": {
      "submit_for_settlement": True
    }
    })
    
    print(result)
    print(request.form)
    send_message()
    return redirect(url_for('users.show', username = current_user.name))