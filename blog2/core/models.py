from django.db import models

# Create your models here.
class User(models.Model):
    id = models.CharField(max_length=64)
    username = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    password = models.CharField(max_length=64)
    information = models.CharField(max_length=1024)

class Comment(models.Model):
    author = models.CharField(max_length=128)
    pubTime = models.DateTimeField()
    context = models.CharField()

class Archive(models.Model):
    id = models.CharField(max_length=64)
    title = models.CharField(max_length=512)
    context = models.CharField()
    author = models.CharField(max_length=128)
    pubTime = models.DateTimeField()
    editTime = models.DateTimeField()
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE)
