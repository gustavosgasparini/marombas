from django.db import models
from accounts.models import User

# Create your models here.

class Post(models.Model):

    author  = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField('Created', auto_now_add=True)
    updated = models.DateTimeField('Updated', auto_now=True)
    text    = models.TextField('Text', blank=True)
    image   = models.ImageField('Image', upload_to='img_post', null=True, blank=True)


class Comment(models.Model):

    author  = models.ForeignKey(User, on_delete=models.CASCADE)
    post    = models.ForeignKey(Post, on_delete=models.CASCADE)
    text    = models.TextField('Comment', blank=True)
    created = models.DateTimeField('Created', auto_now_add=True)
