from django.urls import path
from . import views

from.views import *
urlpatterns = [
    path("", views.index,name="index"),
    path("contact/", views.contact, name="contact"),
    path("blogs/",views.blogs, name='blogs'),
    path("add_post/", views.add_post, name='add_post'),
    path("bloglist/",views.BlogListView.as_view(),name="bloglist"),
    path("editors/",editor_list,name = "editors"),
]
