from mongoengine import Document, StringField, IntField, EmailField

class User(Document):
    name = StringField(required=True)
    email = EmailField()
