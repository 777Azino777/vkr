from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Out_message(models.Model):
    out_messages = models.ForeignKey(User, on_delete='')
    name_user = models.CharField(max_length = 50)

class Message_User(models.Model):
    in_messages = models.ForeignKey(User,on_delete='')
    out_messages = models.ForeignKey(Out_message,on_delete='')
    text_messages = models.TextField()

class Person(models.Model):
    user_id = models.ForeignKey(User,on_delete='')
    firs_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)

class anonim_message(models.Model):
    text_message = models.TextField(verbose_name="Раскажите свою историю")
    nickname_message = models.CharField(max_length = 50)
