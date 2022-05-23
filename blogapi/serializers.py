from click import password_option
from rest_framework.serializers import ModelSerializer
from baseapp.models import Post, User
from rest_framework import serializers

#c=Post.objects.get(id=1)
#c.author.add(1)
class PostSerializer(ModelSerializer):
    
    class Meta:
        model = Post
        fields = '__all__'


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id','email', 'username', 'password']

    def create(self, validated_data):
        # password = validated_data['password']
        instance = self.Meta.model(**validated_data)
        # password = validated_data.pop('password')
        # print(password)
        # validated_data['password'] = 101233
        instance.set_password('8888')
        print(validated_data)
        instance.save()
        return instance
    
    def update(self, instance, validated_data):
        print(validated_data.get('email', instance.email))
        instance.email = validated_data.get('email', instance.email) + 'm'
        instance.save()
        return instance

        
class PostSerializer1(ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True, many=False)
    #author = serializers.StringRelatedField()
    author = UserSerializer(read_only=True, many=False)
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


class UserPostSerialiser(serializers.Serializer):
    user_serializer = UserSerializer(many=True)
    posts_serializer = PostSerializer(many=True)