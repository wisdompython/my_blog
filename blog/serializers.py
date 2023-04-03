from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from django.db import models
from .models import BlogPost, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    class Meta:
        model = BlogPost
        fields= '__all__'
