from django.db import models
from django.contrib.auth.models import User

class Lesson(models.Model):
    name = models.CharField(max_length=70)
    file = models.FileField(upload_to='files/',null=True, blank=True)
    description = models.TextField()
    users = models.ManyToManyField(User)
