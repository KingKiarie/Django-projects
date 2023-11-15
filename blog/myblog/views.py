from urllib import response
from django.shortcuts import render,redirect
from myblog.forms import BlogForm
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


# Create your views here.
def index(request):
    return render(request,'index.html')
def contact(request):
    return render(request,'contact.html')
def blogs(request):
    blogs = Blog.objects.all()
    ctx  = {"blogs": blogs}

    return render(request,'blogs.html',ctx)

def add_post(request):
    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            
            blog.save()

            form = BlogForm()

            return redirect("/blogs")
        
    else:
        form = BlogForm()


    return render(request, "form.html", {"form": form})


@api_view(["Get","POST"])

def editor_list(request):
    if request.method == "GET":
        editors = Editor.objects.all()
        serializer = EditorSerializer(editors,many=True)
        
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = EditorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#API view
class BlogListView(APIView):
    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer= BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    