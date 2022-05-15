from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(unique=True, )
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Post(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    author = models.ManyToManyField(User,related_name='author')#, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='image', null=True) #, default='den.jpg')
    date_posted = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name




