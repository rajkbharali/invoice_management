from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    TYPE_OF_ACCESS = [
        ('agent', 'Agent'),
        ('manager', 'Manager')
    ]
    access_type = models.CharField(choices=TYPE_OF_ACCESS,
                                   default=TYPE_OF_ACCESS[0][0],
                                   max_length=20)


    def __str__(self):
        return f'Access: {self.access_type} User: {self.user}'

