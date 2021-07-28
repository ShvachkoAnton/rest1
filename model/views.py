
# Create your views here.
from .permissions import IsAuthorOrReadOnly
from django.shortcuts import get_object_or_404,render
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser 
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status,renderers
from rest_framework.views import APIView 
from .serializers import Postserializer,Userserializer
from django.http import JsonResponse, request, Http404
from .models import Post
from .permissions import IsAuthorOrReadOnly
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import permissions
from rest_framework.reverse import reverse
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
        serializer_context = {
            'request': request,
        }
        snippets=Post.objects.all()
        serializer=Postserializer(snippets,context=serializer_context, many=True)
        return  Response(serializer.data)
    def post(self,request,format=None):
        serializer=Postserializer(data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self,serializer): #связь с автором
        serializer.save(author=self.request.user)

class List_detail(APIView):
    def get_object(self,pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404
    def get(self,request, pk, format=None):
        snippet=self.get_object(pk)
        serializer_context = {
            'request': request,
        }
        serializer=Postserializer(snippet,context=serializer_context)
        return Response(serializer.data)
    def put(self,request,pk,format=None):
        snippet=self.get_object(pk)
        serializer_context = {
            'request': request,
        }
        serializer=Postserializer(snippet,context=serializer_context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        snippet=self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    permission_classes=[permissions.IsAuthenticatedOrReadOnly,IsAuthorOrReadOnly]



class UserList(generics.ListAPIView):
    queryset=User.objects.all()
    serializer_class=Userserializer
class UserDetail(generics.RetrieveAPIView):
    queryset=User.objects.all()
    serializer_class=Userserializer



@api_view(['GET'])
def api_root(request,format=None):
    return Response({
    'users':reverse('user-list',request=request,format=format),
    'posts':reverse('snippet-list',request=request,format=format)

    }) #конечные точки для api


class PostHighlight(generics.GenericAPIView):
    queryset=Post.objects.all()
    renderer_classes=[renderers.StaticHTMLRenderer]
    def get(self,request,*args,**kwargs):
        post=self.get_object()
        return Response(post.highlight)
