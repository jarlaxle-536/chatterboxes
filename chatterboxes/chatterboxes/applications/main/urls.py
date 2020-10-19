from django.urls import path

from .views import *

urlpatterns = [
    path(
        '',
        MainPageAPI.as_view(),
        name='main'
    ),
    path(
        'settings',
        SettingsAPI.as_view(),
        name='chat_settings'
    ),
    path(
        'chat',
        ChatAPI.as_view(),
        name='chat'
    )
]
