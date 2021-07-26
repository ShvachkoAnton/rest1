
# Create your views here.
from django.shortcuts import get_object_or_404,render
from rest_framework.response import Response
from rest_framework.parsers import JSONParser 
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.views import APIView 
from .serializers import Postserializer
from django.http import JsonResponse, request, Http404
from .models import Post
from rest_framework.decorators import api_view
"""@api_view(['GET', 'POST'])
def post_view(request):
    
    List all code snippets, or create a new snippet.
    
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
def post_detail(request,pk):
    try:
        snippets=Post.objects.get(pk=pk)
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
        return Response(status=status.HTTP_204_NO_CONTENT)"""



class List(APIView):
    def get(self,request, format=None):
        snippets=Post.objects.all()
        serializer=Postserializer(snippets,many=True)
        return  Response(serializer.data)
    def post(self,request,format=None):
        serializer=Postserializer(data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class List_detail(APIView):
    def get_object(self,pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404
    def get(self,request, pk, format=None):
        snippet=self.get_object(pk)
        serializer=Postserializer(snippet)
        return Response(serializer.data)
    def put(self,request,pk,format=None):
        snippet=self.get_object(pk)
        serializer=Postserializer(snippet,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        snippet=self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
