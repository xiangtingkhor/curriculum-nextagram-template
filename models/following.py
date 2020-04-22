from models.base_model import BaseModel
from models.user import User
import peewee as pw

class Following(BaseModel):
    idol = pw.ForeignKeyField(User)
    follower = pw.ForeignKeyField(User)
    approved = pw.BooleanField(default=False)

    def validate(self):
        if self.idol_id == self.follower_id:
            self.errors.append('Cannot follow self.')