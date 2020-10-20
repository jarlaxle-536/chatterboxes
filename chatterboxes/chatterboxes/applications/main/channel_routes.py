from django.urls import path

from .consumers import *

urlpatterns = [
    path('chat/', ChatConsumer),
]
