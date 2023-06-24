from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('typography/', typography, name='typography'),
]