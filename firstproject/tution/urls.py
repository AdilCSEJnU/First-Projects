
from django.urls import path
from .views import contact, postview, postcreat

urlpatterns = [
    path('contact/',contact,name="contact"),
    path('posts/',postview,name="posts"),
    path('creat/',postcreat,name="creat"),


]