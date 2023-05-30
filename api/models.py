from django.db import models
from django.contrib.auth.models import User

class Tasks(models.Model):
    name = models.CharField(max_length=50)
    file = models.FileField(upload_to='files/')
    description = models.TextField()
    rating = models.FloatField()
    status = models.CharField(max_length=40)
class SendTask(models.Model):
    file = models.FileField(upload_to='hwk/')
    task = models.ForeignKey(Tasks,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
class Rating(models.Model):
    rate = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hwk = models.ForeignKey(SendTask, on_delete=models.CASCADE)
class Books(models.Model):
    name = models.CharField(max_length=125)
    file = models.FileField()