
# Create your views here.
from django.shortcuts import get_object_or_404,render
from rest_framework.response import Response
from rest_framework.parsers import JSONParser 
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status 
from .serializers import Postserializer
from django.http import JsonResponse, request
from .models import Post
from rest_framework.decorators import api_view
@api_view(['GET', 'POST'])
def post_view(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Post.objects.all()
        serializer = Postserializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Postserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])
def post_detail(request,id):
    try:
        snippets=Post.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer=Postserializer(snippets)
        return Response(serializer.data)

    elif request.method=='PUT':
        serializer=Postserializer(snippets, data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        serializer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)