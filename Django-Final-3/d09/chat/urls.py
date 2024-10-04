from django.urls import path
from .views import chat_room_list, chat_room_detail, create_chat_room

urlpatterns = [
    path('chat/', chat_room_list, name='chat_room_list'),
    path('chat/<int:id>/', chat_room_detail, name='chat_room_detail'),
    path('', chat_room_list, name='chat_room_list'),
    path('room/<int:room_id>/', chat_room_detail, name='chat_room_detail'),
    path('create/', create_chat_room, name='create_chat_room'),

]
