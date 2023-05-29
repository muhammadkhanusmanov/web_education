from django.contrib import admin
from .models import Lesson,Status,SendTask,Rating,Books
from rest_framework.authtoken.models import Token

admin.site.register([Lesson,Status,SendTask,Rating,Books])
