from django.contrib.auth.models import User
from django.db import models


class Message(models.Model):
    title = models.CharField(max_length=30)
    message_body = models.TextField(null=True, blank=True)
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    date = models.DateField()
    id = models.AutoField(primary_key=True)

