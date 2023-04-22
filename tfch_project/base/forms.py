from django.forms import ModelForm
from .models import ChatRoom, User, Pianist, Program, Concert
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
        fields = '__all__'
        exclude = ['pianist','programs']

class ProgramForm(ModelForm):
    class Meta:
        model = Program
        fields = '__all__'
        exclude = ['compositions']

class ConcertForm(ModelForm):
    class Meta:
        model = Concert
        fields = '__all__'

class ProgramModificationForm(ModelForm):
    class Meta:
        model = Program
        fields = '__all__'
        exclude = ['compositions']