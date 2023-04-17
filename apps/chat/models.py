from django.db import models
from django.utils.crypto import get_random_string

from apps.common.models import BaseModel
from django.utils.translation import gettext as _


class Chat(BaseModel):
    name = models.CharField(verbose_name=_("Name"), max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name if self.name else ""

    def save(self, *args, **kwargs):
        if self.name is None:
            self.name = get_random_string(20)
        super(Chat, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Chat"
        verbose_name_plural = "Chats"


class Participant(BaseModel):
    user = models.ForeignKey('account.Account', verbose_name=_("User"), on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, verbose_name=_("Chat"), on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Participant"
        verbose_name_plural = "Participants"


class Message(BaseModel):
    chat = models.ForeignKey(Chat, verbose_name=_("Chat"), on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey('account.Account', verbose_name=_("Sender"), on_delete=models.CASCADE)
    msg = models.TextField(verbose_name=_("Message"), )
    is_read = models.BooleanField(verbose_name=_("Is read?"), default=False)

    def __str__(self):
        return self.sender.username

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"
