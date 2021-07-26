from django.db.models.base import ModelState
from rest_framework import serializers
from model.models import Post
class Postserializer(serializers.ModelSerializer):
    class Meta:
        fields=('text','author','pub_date')
        model=Post
