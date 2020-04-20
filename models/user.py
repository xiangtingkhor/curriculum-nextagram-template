from models.base_model import BaseModel
import peewee as pw
import re
from werkzeug.security import generate_password_hash
from flask_login import UserMixin, current_user, login_user
from playhouse.hybrid import hybrid_property

def is_upper_case(word):
    arr = []
    for char in word:
        if char.isupper():
            arr.append(char)
    
    return len(arr)
            

def is_lower_case(word):
    arr = []
    for char in word:
        if char.islower():
            arr.append(char)
        
    return len(arr)

def no_special_case(word):
    if len(re.findall('[^a-zA-Z0-9]', word)) == 0:
        return True 
    else:
        return False


class User(UserMixin, BaseModel):
    name = pw.CharField(unique=False, null = False)
    email = pw.CharField(null = True)
    password = pw.TextField( null = True)
    profile_img = pw.CharField( null = False, default='default.jpg')

    @hybrid_property
    def profile_img_url(self):
        from app import app
        if self.profile_img == None:
            return "#"
        else:
            return app.config.get('AWS_S3_DOMAIN') + self.profile_img

    def validate(self):
        duplicate_name = User.get_or_none(User.name == self.name)
        check_name_length = len(self.name)
        check_password_length = len(self.password)

        if duplicate_name and not duplicate_name.id == self.id:
            self.errors.append("This name has already exist.")
        if is_upper_case(self.password) == 0:
            self.errors.append("Password must have at least 1 upper case character.")
        if is_lower_case(self.password) == 0:
            self.errors.append("Password must have at least 1 lower case character.")
        if no_special_case(self.password):
            self.errors.append("Password must have at least 1 special character.")
        if check_name_length < 6:
            self.errors.append("username must be 6 characters and above")
        if check_password_length < 6:
            self.errors.append("password must be 6 characters and above")
        else:
            self.password = generate_password_hash(self.password)

        




