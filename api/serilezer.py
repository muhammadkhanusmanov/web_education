from rest_framework import serializers
from .models import Lesson,Status

class LessonSerializer(serializers.ModelSerializer):
    status = serializers.SlugField(many=True,read_only=True)

    class Meta:
        model = Lesson
        fields = ['id', 'name','file','description','status']

    