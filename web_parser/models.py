from mongoengine import *

class ParsedPage(Document):
    user = ReferenceField(User)
    time = DecimalField()
