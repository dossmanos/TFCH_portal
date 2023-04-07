from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)

    avatar = models.ImageField(null=True, default='avatar.svg')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

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