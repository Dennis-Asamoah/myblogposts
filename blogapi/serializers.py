from rest_framework.serializers import ModelSerializer
from baseapp.models import Post, User


class PostSerializer(ModelSerializer):
    
    class Meta:
        model = Post
        fields = '__all__'


class UserSerializer(ModelSerializer):
    author =  PostSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'author'] 





    