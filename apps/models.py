from django.db import models
from django.conf import settings
from django.utils import timezone 
# Create your models here.

class ProfileUser(models.Model):
    user  = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE   )
    image = models.ImageField(upload_to='image')
    bio = models.TextField(max_length=230)
    
    def __str__(self) -> str:
        return self.user.username
     

class Category(models.Model):
    name= models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.name

class Posts(models.Model):
    user         = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE   )
    category     = models.ForeignKey(Category, on_delete=models.CASCADE,  null=True)
    title        = models.CharField(max_length=200, blank=False, )
    description  = models.TextField(max_length=100, blank=False,  )
    slug         = models.SlugField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=False , default=timezone.now )
    
    def __str__(self):
        return self.title
class Comment(models.Model):
    user         = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    text_comment = models.TextField(max_length=200, blank=True)
    post         = models.ManyToManyField(Posts)
    date_created = models.DateTimeField(auto_now_add=False,)
    
    def __str__(self):
        return self.text_comment
    
        
      