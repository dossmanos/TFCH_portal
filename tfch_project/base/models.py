from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Composition(models.Model):
    polish_name:str = 'any'
    english_name:str = 'any'
    name:list = [
        {'polski': polish_name},
        {'english': english_name},
    ]

    def __init__(self, pol_composition_name, eng_composition_name):
        self.name =[
            {'polski':pol_composition_name},
            {'english':eng_composition_name},
        ]
    def __str__(self):
         return self.name()   
    
class ChopinPieces(models.Model):
    pieces: list[Composition] = []

class Pianist(models.Model):
    pianist = models.OneToOneField(User,on_delete=models.CASCADE)
    program = models.TextField(max_length=1500)

    next_concert = models.DateField(name='next_concert')
    def __str__(self):
        return self.pianist.get_full_name()
    avatar = models.ImageField(null=True, default='avatar.svg')

class ChatTopic(models.Model):
    topic_name = models.CharField(max_length=200)

    def __str__(self):
        return self.topic_name

class ChatRoom(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    room_topic = models.ForeignKey(ChatTopic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=180)
    description = models.TextField(null=True, blank=True)
    chat_participants = models.ManyToManyField(User, related_name='chat_participants', blank=True)
    updating = models.DateTimeField(auto_now=True)
    creating = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updating', '-creating']

    def __str__(self):
        return self.name

class SystemMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)   
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    message_text = models.TextField()
    updating = models.DateTimeField(auto_now=True)
    creating = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updating', '-creating']

    def __str__(self):
        return self.message_text[0:50]