from django.contrib import admin
from .models import SendTask,Rating,Tasks,Books

admin.site.register([SendTask,Rating,Tasks,Books])
