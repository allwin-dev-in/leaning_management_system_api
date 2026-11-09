from django.contrib.auth.models import User

from rest_framework import serializers

from course_management.models import Course

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","email","password"]

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields="__all__"
        read_only_fields=["id","created_at"]

