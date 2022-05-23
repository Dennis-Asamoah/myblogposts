from collections import namedtuple
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.response import Response
from .serializers import PostSerializer, UserPostSerialiser, UserSerializer, UserSerializer1,  PostSerializer1
from baseapp.models import Post, User
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissionsOrAnonReadOnly,DjangoModelPermissions, AllowAny
from rest_framework import  generics
from rest_framework.views import APIView
from blogapi import serializers
from rest_framework.parsers import  MultiPartParser, FormParser
from rest_framework import status
from rest_framework_simplejwt.tokens import  RefreshToken
from django.contrib.auth.hashers import make_password, check_password


UserPost = namedtuple('UserPost', ['user_serializer','posts_serializer'])

# Create your views here.
@api_view(['GET', 'POST'])
#@permission_classes([IsAuthenticated])
#@parser_classes([MultiPartParser, FormParser])
def list_posts(request):
    
    if request.method == 'GET':
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many = True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        data = request.data
       # print(data)
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

@api_view(['POST'])
@permission_classes([AllowAny])    
def  register_user(request):
    ## We can do a check here  like comparing passwords and checking if email already or username exits 

    data = request.data
    print(123456)
    print(data)
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response('was succesfully created',status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def blacklist(request):
    try:
        print(request.data)
        data = request.data['refresh_token']
        token = RefreshToken(data)
        token.blacklist()
        return Response('done')
    except Exception as e:
        print(str(e))
        return Response(status=status.HTTP_400_BAD_REQUEST)   

@api_view(['GET'])
def foreign(request):
    user = Post.objects.all()
    serializer = PostSerializer1(user, many=True)
    return Response(serializer.data)

class Foreign(generics.ListAPIView):
    permission_classes = [IsAuthenticated] 
    queryset = User.objects.all()
    serializer_class = UserSerializer1 


class Filter(APIView):

    def get(self, request):
        post = Post.objects.all()
        user = User.objects.all()
        user_post = UserPost(user_serializer=user, posts_serializer=post) 
        serializer =  UserPostSerialiser(user_post)
        print (serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RegisterUser(APIView):
    def post(self, request):
        data = request.data 
        serializer =  UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUES)

class Authors(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AuthorView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

 
