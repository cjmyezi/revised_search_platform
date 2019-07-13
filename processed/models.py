from django.db import models
from mongoengine import StringField, DateTimeField
# Create your models here.


class DetailPage(models.Model):
    url = StringField(unique=True, required=True)
    time = DateTimeField(required=True)
    html = StringField(required=True)
    
    