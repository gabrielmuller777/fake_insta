from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


class Profile(models.Model):
    user = models.OneToOneField(User, null = True, on_delete = models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return str(self.user)

class Post(models.Model):
    description  = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.description + ' | ' + str(self.author)


