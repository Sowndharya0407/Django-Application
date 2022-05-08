from django.db import models
from django.contrib.auth.models import User   #reference to user table

# Create your models here.

class BlogPost(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.TextField(max_length=100,null=True)
    body = models.TextField(max_length=100,null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
