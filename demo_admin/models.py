from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DemoAdmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default=None)
    is_active = models.BooleanField(default=True)