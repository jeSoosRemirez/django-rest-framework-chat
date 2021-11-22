from django.db import models


class Message(models.Model):
    author = models.CharField(max_length=100, blank=True, default='Anon')
    author_email = models.EmailField(max_length=254, blank=True, default='')
    text = models.TextField(max_length=100, blank=False)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_time']
