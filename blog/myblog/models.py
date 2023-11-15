from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Editor(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    bio = models.CharField(max_length=500)
    editorPhoto = CloudinaryField("editorPhoto",null=True) 
    

class Blog(models.Model):
    # first_name = models.CharField(max_length=255 )
    # last_name = models.CharField(max_length=255)
    # email = models.EmailField(max_length=255)
    title = models.CharField(max_length=255)
    editor = models.ForeignKey(Editor,on_delete=models.SET_NULL,null=True)
    text = models.TextField(max_length=2000)
    photo = CloudinaryField('photo',null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True,null=True)
    
    def __str__(self):
        return self.title