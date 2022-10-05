from django.urls import path
from vigenere.views import HomeIndex, encode

urlpatterns = [
    path('', HomeIndex.as_view(), name='home'),
    path('encode/',encode, name='encode'),
]