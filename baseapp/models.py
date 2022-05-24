from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import  slugify


options = (
    ('published','Pusblished'),
    ('pending','Pending'),
    # (1,2),
    # (12,56)
    
)

class User(AbstractUser):
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(unique=True, )
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        self.password += 'mmm'
        super(User, self).save(*args, **kwargs)


class Post(models.Model):
    name = models.CharField(max_length=200)# null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    #author = models.ManyToManyField(User,related_name='author')#, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank= True)
    image = models.ImageField(upload_to='image', null=True, blank=True) #, default='den.jpg')
    date_posted = models.DateTimeField(auto_now = True)
    published = models.CharField(max_length=200,choices=options,null=True, blank=True)
    slug = models.SlugField(null=True, unique=True, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name) + '-me'
            print(self.slug )
            super(Post, self).save(*args, **kwargs)




