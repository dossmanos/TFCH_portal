from django.forms import ModelForm
from .models import ChatRoom, User, Pianist
from django.contrib.auth.forms import UserCreationForm

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']

class ChatRoomForm(ModelForm):
    class Meta:
        model = ChatRoom
        fields = '__all__'
        exclude = ['host', 'chat_participants']

class UserForm(ModelForm):
    class Meta:
        model = Pianist
        fields = ['program']