from django.urls import path

from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('settings', settings, name='chat_settings'),
]
