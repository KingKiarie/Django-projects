from rest_framework import serializers
from .models import Blog
from .models import Editor

class EditorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editor
        fields = "__all__"

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        editor = EditorSerializer # so that we can be able to nest our data for blog
        model = Blog
        fields = "__all__"
    
    def create(self, validated_data):
        editor_data = validated_data.pop("editor")
        
        editor = Editor.object.create(**editor_data)
        
        blog = Blog.objects.create(editor= editor, **validated_data)
        
        return blog
    