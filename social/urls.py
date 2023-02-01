from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",index , name='index'),
    path("register", register , name='register'),
    path("login", login , name='login'),
    path("home", home , name='home'),
    path("create_post", create_post , name='create_post'),
    path("logout", logout , name='logout'),
    path("change/dp", handle_dp , name='handle_dp'),
]

urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
