from mongoengine import *
from user_system.models import *
import datetime

class InteractionTrace(DynamicDocument):
    user = ReferenceField(User)
    start = DateTimeField(default=datetime.datetime.now())
    end = DateTimeField(default=datetime.datetime.now())
    dwell_time = FloatField()
    page_timestamps= ListField(DictField())
    type=StringField()
    origin=StringField()
    url=StringField()
    serp_link=StringField()
    query=StringField()
    clicked_results=ListField(DictField())
    mouse_moves=ListField(DictField())
