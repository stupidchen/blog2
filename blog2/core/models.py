from django.db import models

class DictMixin(object):
    default_columns = []

    def as_dict(self, columns=None):
        if not columns:
            columns = self.default_columns
        ret = {}
        for column in columns:
            try:
                value = getattr(self, column)
                ret[column] = value
            except:
                pass
        return ret

# Create your models here.
class User(models.Model, DictMixin):
    id = models.CharField(max_length=32, primary_key=True)
    username = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    password = models.CharField(max_length=64)
    information = models.TextField()
    default_columns = ['username', 'email', 'information']

    def __str__(self):
        return 'User ' + self.id + ' with name ' + self.username

class Comment(models.Model, DictMixin):
    id = models.CharField(max_length=32, primary_key=True)
    author = models.CharField(max_length=128)
    pubTime = models.DateTimeField()
    content = models.TextField()
    default_columns = ['author', 'pubTime', 'content']

    def __str__(self):
        return 'Comment ' + self.id + ' by ' + self.author


class Archive(models.Model, DictMixin):
    id = models.CharField(max_length=32, primary_key=True)
    title = models.TextField()
    content = models.TextField()
    author = models.CharField(max_length=128)
    pubTime = models.DateTimeField()
    editTime = models.DateTimeField()
    default_columns = ['title', 'content', 'author', 'pubTime', 'editTime']

    def __str__(self):
        return 'Archive ' + self.id + 'by ' + self.author

class Archive_Comment_Relation(models.Model):
    archive_id = models.ForeignKey(Archive, on_delete=models.CASCADE)
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)
