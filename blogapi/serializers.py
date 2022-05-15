from rest_framework.serializers import ModelSerializer
from baseapp.models import Post, User
from rest_framework import serializers

c=Post.objects.get(id=1)
c.author.add(1)
class PostSerializer(ModelSerializer):
    
    class Meta:
        model = Post
        fields = '__all__'


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id','email', 'username'] 


class PostSerializer1(ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True, many=False)
    #author = serializers.StringRelatedField()
    author = UserSerializer(read_only=True, many=True)
    #print(author)
    class Meta:
        model = Post
        fields = ['id', 'name', 'author']


class UserSerializer1(ModelSerializer):
    #author = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    #posts = UserSerializer()#(many=True,read_only=True)
    author = PostSerializer1(many=True, read_only=True)
    k=56
    class Meta:
        
        model = User
        fields = ['id','email', 'username', 'author',] 


    