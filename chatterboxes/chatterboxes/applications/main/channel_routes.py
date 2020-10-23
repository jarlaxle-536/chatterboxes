from django.urls import path

from .consumers import *

urlpatterns = [
    path('general/', GeneralConsumer),
    path('chat/', ChatConsumer),    
]
