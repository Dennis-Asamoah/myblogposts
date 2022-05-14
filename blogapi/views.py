from urllib import response
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.response import Response
from .serializers import PostSerializer, UserSerializer
from baseapp.models import Post, User
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissionsOrAnonReadOnly,DjangoModelPermissions
from rest_framework import  generics
from rest_framework.views import APIView
from blogapi import serializers
from rest_framework.parsers import  MultiPartParser, FormParser
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
#@permission_classes([DjangoModelPermissions])
#@parser_classes([MultiPartParser, FormParser])
def list_posts(request):
    
    if request.method == 'GET':
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many = True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        data = request.data
        serializer = PostSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


# class ListPost(APIView):
    
#     queryset = Post.objects.all()
#     permission_classes = [DjangoModelPermissions]

#     def get(self,request):
#         queryset = Post.objects.all()
#         serializer = PostSerializer(queryset, many = True)

#         return Response(serializer.data)

#     def post(self,request):
#         data = request.data
#         serializer = PostSerializer(data = data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)

#         return Response('400') 

class ListPost(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class  = PostSerializer
    #permission_classes = [DjangoModelPermissions]
       
class DetailedView(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class  = PostSerializer
    #permission_classes = [DjangoModelPermissions]

@api_view(['GET', 'PUT', 'DELETE'])
#@permission_classes([DjangoModelPermissions])
#@permission_classes([MultiPartParser, FormParser])
def detailed_view(request,id):
    post = Post.objects.get(id = id)

    if request.method == 'GET':
        serializer = PostSerializer(post, many = False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif  request.method == 'PUT':
        serializer = PostSerializer(instance = post, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    else:
        post.delete()
        return Response('post was deleted succesfully')
    

   

