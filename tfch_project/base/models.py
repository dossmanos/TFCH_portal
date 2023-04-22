from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.
class Composition(models.Model):
    polish_name:str = models.TextField(max_length=100, null=True)
    english_name:str = models.TextField(max_length=100, null=True)
    name:list[dict] = [
        {'polski': polish_name},
        {'english': english_name},
    ]

    def __str__(self):
        return self.polish_name
    
class Program(models.Model):
    program_pianist = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100, null=True, unique=True)
    compositions = models.ManyToManyField(Composition, related_name='compositions', blank=True)
    def __str__(self):
        return self.name    

class Pianist(models.Model):
    pianist = models.OneToOneField(User,on_delete=models.CASCADE, null=True)
    programs = models.ManyToManyField(Program, related_name='programs',blank=True)
    avatar = models.ImageField(null=True, default='avatar.svg')
    def __str__(self):
        return self.pianist.get_full_name()

class Concert(models.Model):
    concert_pianist = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    concert_program = models.ForeignKey(Program, on_delete=models.SET_NULL, null=True)
    concert_date = models.DateTimeField(default=datetime.datetime.now())
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