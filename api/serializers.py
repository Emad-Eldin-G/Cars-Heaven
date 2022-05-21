from rest_framework import serializers
from .models import *

class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = "__all__"

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = blog
        fields = "__all__"
