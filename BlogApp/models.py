from django.contrib.auth.models import PermissionsMixin, User
from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=30)
    subtitle = models.CharField(max_length=30)
    body = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    picture = models.ImageField(null=True, blank=True, upload_to="images/")
    id = models.AutoField(primary_key=True)


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ImageField(null=True, blank=True, upload_to="images/profile")
    description = models.TextField(null=True, blank=True)
    link = models.CharField(max_length=30)

    objects = models.Manager()

    def __str__(self):
        return self.user.username

