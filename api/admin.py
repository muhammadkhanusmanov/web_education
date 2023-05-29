from django.contrib import admin
from .models import Lesson,Status
from rest_framework.authtoken.models import Token

admin.site.register([Lesson,Status])
