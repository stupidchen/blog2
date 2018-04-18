from django.db import models

# Create your models here.
class User(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    username = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    password = models.CharField(max_length=64)
    information = models.TextField()

    def __str__(self):
        return 'User ' + self.id + ' with name ' + self.username

class Comment(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    author = models.CharField(max_length=128)
    pubTime = models.DateTimeField()
    content = models.TextField()

    def __str__(self):
        return 'Comment ' + self.id + ' by ' + self.author


class Archive(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    title = models.TextField()
    content = models.TextField()
    author = models.CharField(max_length=128)
    pubTime = models.DateTimeField()
    editTime = models.DateTimeField()

    def __str__(self):
        return 'Archive ' + self.id + 'by ' + self.author

class Archive_Comment_Relation(models.Model):
    archive_id = models.ForeignKey(Archive, on_delete=models.CASCADE)
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)
