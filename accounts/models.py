from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    shopname = models.CharField(max_length=20, unique=True)
    money = models.IntegerField(default=100000)
    rank = models.IntegerField(default=5010)
    showcase_count = models.IntegerField(default=1)
    foundation = models.DateTimeField(auto_now_add=True)
    icon = models.IntegerField(default=1)

    def __str__(self):
        return self.username