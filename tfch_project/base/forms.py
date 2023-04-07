from django.forms import ModelForm
from .models import ChatRoom, User
from django.contrib.auth.forms import UserCreationForm

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name','username','email','password1','password2']

class ChatRoomForm(ModelForm):
    class Meta:
        model = ChatRoom
        fields = '__all__'
        exclude = ['host', 'chat_participants']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar','name','username','email','bio']