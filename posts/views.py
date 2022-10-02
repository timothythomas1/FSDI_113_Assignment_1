from django.views.generic import (
    ListView, 
    DetailView
) 
from django.views.generic.edit import (
    DeleteView, 
    CreateView, 
    UpdateView
)

from .models import Post
from django.urls import reverse_lazy
# more info:
# https://docs.djangoproject.com/en/4.1/ref/urlresolvers/
# This looks up a url pattern via its name tag, but waits until the underlying database transaction is complete

# Create your views here.
class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post

class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post

class PostCreateView(CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title", "subtitle", "author", "body"]

class PostUpdateView(UpdateView):
    template_name = "posts/edit.html"
    model = Post
    fields = ["title", "subtitle", "author", "body"] # Fields will be showed on the page
# delete view for details

class PostDeleteView(DeleteView):
    model = Post
    # success_url ="/posts" # You can specify success urlurl to redirect after successfully
    template_name = "posts/confirm_delete.html" # deleting object
    success_url = reverse_lazy("list")
