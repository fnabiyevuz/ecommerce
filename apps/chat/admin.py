from django.contrib import admin
from .models import Chat, Participant, Message


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    date_hierarchy = 'created_at'


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'chat')
    list_display_links = ('id', 'user', 'chat')
    date_hierarchy = 'created_at'


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'chat', 'sender', 'msg', 'is_read')
    list_display_links = ('id', 'chat', 'sender')
    date_hierarchy = 'created_at'
