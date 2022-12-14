from django.db import models
import uuid

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    repeatpassword = models.CharField(max_length=20)

    
class Login(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id=models.ForeignKey(User, on_delete = models.SET_NULL, null =True)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)