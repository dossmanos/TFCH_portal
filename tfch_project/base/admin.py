from django.contrib import admin

# Register your models here.
from .models import ChatRoom, ChatTopic, SystemMessage, Pianist, Composition, Program

admin.site.register(Pianist)
admin.site.register(Program)
admin.site.register(ChatRoom)
admin.site.register(ChatTopic)
admin.site.register(SystemMessage)
admin.site.register(Composition)