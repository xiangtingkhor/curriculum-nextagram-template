from models.base_model import BaseModel
from models.user import User
import peewee as pw
from playhouse.hybrid import hybrid_property
import os

#need to import user to state where you get the ForeignKeyField
class Images (BaseModel):
    img = pw.CharField()
    user = pw.ForeignKeyField(User, backref='images')
    
    @hybrid_property
    def img_url(self):
        from app import app
        return app.config.get('AWS_S3_DOMAIN') + self.img
        
