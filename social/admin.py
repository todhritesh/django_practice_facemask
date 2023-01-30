from django.contrib import admin
from .models import Account , Post
# Register your models here.
admin.site.register([Account,Post])
