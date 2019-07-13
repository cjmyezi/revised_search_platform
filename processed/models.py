from django.db import models
from mongoengine import StringField, DateTimeField
from mongoengine import *
# Create your models here.


class DetailPage(Document):
    url = StringField(unique=True, required=True)
    time = DateTimeField(required=True)
    html = StringField(required=True)
    
    