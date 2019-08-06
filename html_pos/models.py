from django.db import models
from mongoengine import StringField, DateTimeField, IntField
from mongoengine import *
# Create your models here.


class ItemPos(Document):
    item_id = IntField(unique=True, required=True)
    result_type = StringField(required=True)
    left = IntField(required=True)
    top = IntField(required=True)
    width = IntField(required=True)
    height = IntField(required=True)


class Positions(Document):
    task_id = IntField(unique=True, required=True)
    item_pos = ListField(ItemPos())


class SogouPositions(Document):
    task_id = IntField(unique=True, required=True)
    item_pos = ListField(ItemPos())