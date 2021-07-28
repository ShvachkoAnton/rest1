from django.db.models.base import ModelState
from rest_framework import serializers
from model.models import Post
from django.contrib.auth.models import User
from rest_framework import generics
class Postserializer(serializers.HyperlinkedModelSerializer):
    author=serializers.ReadOnlyField(source='author.username')
    highlight=serializers.HyperlinkedIdentityField(view_name='post-highlight', format='html')
    class Meta:
        model=Post
        fields=['url', 'id','highlight', 'text','author','pub_date',]
        


class Userserializer(serializers.HyperlinkedModelSerializer):
    snippets=serializers.HyperlinkedRelatedField(many=True, view_name='post-detail',read_only=True)    #название должно соответствовать имени модели


    class Meta:
        model=User
        fields=['id','username','url','snippets']