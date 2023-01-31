from django.db import models
from django.contrib.auth.models import User

# Create your models here.
GENDER = (
    ('Male','Male'),
    ('Female','Female'),
    ('Others','Others'),
)
class Account(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    contact = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.CharField(choices=GENDER,max_length=10)


    def __str__(self):
        return self.user
    

class Post(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    createAt = models.DateTimeField(auto_now_add=True)
    caption = models.TextField(null=True)


    def __str__(self):
        return self.user