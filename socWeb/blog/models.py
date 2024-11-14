from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):

    STATUS_CHOICES = [
        ('DF', 'DRAFT'),
        ('PB', 'PUBLISHED')
    ]
    title = models.CharField(max_length=90)
    slug = models.SlugField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_post')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=12,choices=STATUS_CHOICES, default='DF')
