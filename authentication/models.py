from django.db import models
from blog.models import Status
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=140)
    mail = models.EmailField(max_length=140)
    status = models.ManyToManyField(Status)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name