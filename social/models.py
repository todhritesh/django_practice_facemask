from django.db import models
from django.contrib.auth.models import User

# Create your models here.
GENDER = (
    ('Male','Male'),
    ('Female','Female'),
    ('Others','Others'),
)
class Account(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE , primary_key=True)
    contact = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.CharField(choices=GENDER,max_length=10)
    profile_image = models.ImageField( upload_to='profile_images', height_field=None, width_field=None, max_length=None , null=True)


    def __str__(self):
        return self.user.username
    

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    createAt = models.DateTimeField(auto_now_add=True)
    caption = models.TextField(null=True)
    image = models.ImageField(upload_to = 'post_images' , null=True)


    def __str__(self):
        return self.user.username