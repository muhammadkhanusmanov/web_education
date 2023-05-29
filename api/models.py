from django.db import models
from django.contrib.auth.models import User

class Lesson(models.Model):
    name = models.CharField(max_length=70)
    file = models.FileField(upload_to='files/',null=True, blank=True)
    description = models.TextField()
    users = models.ManyToManyField(User)

class Status(models.Model):
    status=models.CharField(max_length=30)
    rating=models.FloatField(default=None)
    lesson=models.ForeignKey(Lesson,on_delete=models.CASCADE,related_name='status')
class Tasks(models.Model):
    name = models.CharField(max_length=50)
    file = models.FileField(upload_to='files/')
    description = models.TextField()
    rating = models.FloatField()
    status = models.CharField(max_length=40)

