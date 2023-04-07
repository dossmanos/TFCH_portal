from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.contrib import messages
from .models import ChatRoom, ChatTopic, SystemMessage, User
from .forms import ChatRoomForm, UserForm, MyUserCreationForm
# Create your views here.

def login_page(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home page')

    if request.method == "POST":
        email=request.POST.get('email')
        password=request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:   
            messages.error(request, 'Specified user does not exist')

        user = authenticate(request, email=email, password=password)    

        if user is not None:
            login(request, user)   
            return redirect('home page')
        else:
            messages.error(request, 'User name or password is INVALID')

    context = {'page':page}    
    return render(request,'base/login_form.html', context)

def logout_page(request):
    logout(request)  
    return redirect('home page')

def register_user(request):
    form = MyUserCreationForm()

    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home page')
        else:
            messages.error(request, "registration failed")

    return render(request, 'base/login_form.html',{'form':form})

def home_page(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''  
    list_of_rooms = ChatRoom.objects.filter(
        Q(room_topic__topic_name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q) |
        Q(host__username__icontains=q)
        )
    room_count = list_of_rooms.count()
    room_messages = SystemMessage.objects.filter(Q(room__room_topic__topic_name__icontains=q))
    topics = ChatTopic.objects.all()[0:5]
    context = {'rooms':list_of_rooms, 'topics':topics, 'room_count':room_count, 'room_messages':room_messages}
    return render(request,'base/home.html',context)

def room(request,primary_key):
    chat_room_number = ChatRoom.objects.get(id=primary_key)  
    room_messages = chat_room_number.systemmessage_set.all() #reference to model SystemMessage
    chat_participants = chat_room_number.chat_participants.all()
    if request.method == "POST":
        message = SystemMessage.objects.create(
            user = request.user,  
            room = chat_room_number,
            message_text = request.POST.get('comment_content')
        )
        chat_room_number.chat_participants.add(request.user)
        return redirect('chat room',primary_key=chat_room_number.id)
    
    dictionary_model = {'room':chat_room_number,'room_messages':room_messages, 'chat_participants':chat_participants}    
    return render(request,'base/chat_room.html',dictionary_model)

def user_profile(request, primary_key):
    user_number = User.objects.get(id=primary_key)
    rooms = user_number.chatroom_set.all()
    room_messages = user_number.systemmessage_set.all()
    topics = ChatTopic.objects.all()
    context = {'user':user_number, 'rooms':rooms, 'room_messages':room_messages, 'topics':topics}
    return render(request,'base/user_profile.html', context)

@login_required(login_url='login')
def create_a_chat_room(request):
    chat_room_form = ChatRoomForm()
    topics = ChatTopic.objects.all()
    if request.method =='POST':
        new_topic_name = request.POST.get('topic')
        topic, creating = ChatTopic.objects.get_or_create(topic_name=new_topic_name)
        ChatRoom.objects.create(
            host = request.user,
            room_topic = topic,
            name = request.POST.get('name'),
            description = request.POST.get('description')
        )
        return redirect('home page')
    context = {'form':chat_room_form, 'topics':topics}
    return render(request,'base/room_form.html', context)

@login_required(login_url='login')
def update_room(request,primary_key):
    chat_room_number = ChatRoom.objects.get(id=primary_key)   
    form = ChatRoomForm(instance=chat_room_number)
    topics = ChatTopic.objects.all()

    if request.user != chat_room_number.host:
        return HttpResponse("Access is not allowed")

    if request.method == 'POST':
        new_topic_name = request.POST.get('topic')
        topic, creating = ChatTopic.objects.get_or_create(topic_name=new_topic_name)
        chat_room_number.name = request.POST.get('name')
        chat_room_number.room_topic = topic
        chat_room_number.description= request.POST.get('description')
        chat_room_number.save()
        return redirect('home page')

    dictionary_model = {'form':form, 'topics':topics, 'room':chat_room_number}   
    return render(request,'base/room_form.html', dictionary_model)

@login_required(login_url='login')
def delete_a_chat_room(request, primary_key):
    chat_room_to_delete = ChatRoom.objects.get(id=primary_key)
    
    if request.user != chat_room_to_delete.host:
        return HttpResponse("Access is not allowed")

    if request.method =='POST':
        chat_room_to_delete.delete()
        return redirect('home page')
 
    return render(request,'base/delete.html', {'obj': chat_room_to_delete})

@login_required(login_url='login')
def delete_a_post(request, primary_key):
    post_to_delete = SystemMessage.objects.get(id=primary_key)
    
    if request.user != post_to_delete.user:
        return HttpResponse("Access is not allowed")

    if request.method =='POST':
        post_to_delete.delete()
        return redirect('home page')
 
    return render(request,'base/delete.html', {'obj': post_to_delete})

@login_required(login_url='login')
def update_user(request): 
    user = request.user  
    form = UserForm(instance=user)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES ,instance=user)
        if form.is_valid():
            form.save()
            return redirect('user profile', primary_key=user.id)
        
    return render(request,'base/update_user.html', {'form':form})

def topics_page(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''  
    topics = ChatTopic.objects.filter(Q(topic_name__icontains=q))
    context = {'topics':topics}
    return render(request, 'base/topics.html', context)

def activities_page(request):
    room_messages = SystemMessage.objects.all()
    return render(request, 'base/activity.html', {'room_messages':room_messages})