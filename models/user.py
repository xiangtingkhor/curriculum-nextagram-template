from models.base_model import BaseModel
import peewee as pw
from werkzeug.security import generate_password_hash
import re


def has_lower(word):
    return re.search("[a-z]", word)

def has_upper(word):
    return re.search("[A-Z]", word)

def has_special(word):
    return re.search("[\W]", word)

class User(BaseModel):
    name = pw.CharField(unique=False)
    username = pw.CharField(unique=True, null = False)
    email = pw.CharField (unique = True, null = False)
    password = pw.CharField (null = False)

#specify whenever you safe the password it will convert it into hash

    def validate(self):
        existing_user = User.get_or_none(email=self.email)

        if existing_user != None:
            self.errors.append("Email is already taken!")

        if len(self.password) < 6:
            self.errors.append("User's password must be more than 6 characters")
        
        if not has_lower(self.password):
            self.errors.append("User's password must have lower case")
        
        if not has_upper(self.password):
            self.errors.append("User's password must have upper case")
        
        if not has_special(self.password):
            self.errors.append("User's password must have special characters")
        
        self.password = generate_password_hash(self.password)


        
