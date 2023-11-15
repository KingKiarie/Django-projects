from dataclasses import fields
from pyexpat import model
from django import forms
from .models import *

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog

        fields = ["title", "text", "photo", "editor"]