from django.urls import path
from .views import *


urlpatterns = [
    path('couple/', couple, name='couple_data_api'),
]