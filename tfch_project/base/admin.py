from django.contrib import admin

# Register your models here.
from .models import ChatRoom, ChatTopic, SystemMessage, User

admin.site.register(User)
admin.site.register(ChatRoom)
admin.site.register(ChatTopic)
admin.site.register(SystemMessage)