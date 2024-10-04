from django.shortcuts import render
from .models import Message, ChatRoom
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def chat_view(request):
    messages = Message.objects.all().order_by('-timestamp')
    return render(request, 'chat/chat.html', {'messages': messages})

@login_required
def chat_room_list(request):
    chat_rooms = ChatRoom.objects.all()
    return render(request, 'chat/chat_room_list.html', {'chat_rooms': chat_rooms})

@login_required
def chat_room_detail(request, room_id):
    room = ChatRoom.objects.get(id=room_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Message.objects.create(room=room, user=request.user, content=content)
        return redirect('chat_room_detail', room_id=room_id)

    messages = Message.objects.filter(room=room).order_by('-timestamp')
    return render(request, 'chat/chat_room_detail.html', {'room': room, 'messages': messages})

@login_required
def create_chat_room(request):
    if request.method == 'POST':
        room_name = request.POST.get('name')
        if room_name:
            room = ChatRoom.objects.create(name=room_name)
            room.participants.add(request.user)
            return redirect('chat_room_detail', room_id=room.id)

    return render(request, 'chat/create_chat_room.html')
