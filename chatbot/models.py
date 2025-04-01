from django.db import models

class UserInput(models.Model):
    text = models.TextField()
    emotion = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)