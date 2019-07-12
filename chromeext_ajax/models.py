from mongoengine import *
from user_system.models import *
import datetime

class InteractionTrace(DynamicDocument):
    user = ReferenceField(User)
    time = DateTimeField(default=datetime.datetime.now())
