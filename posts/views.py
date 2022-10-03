from django.views.generic import (
    ListView, 
    DetailView
    )

from django.views.generic.edit import (
    DeleteView, 
    CreateView, 
    UpdateView
    )

# This is needed for object oriented programming. A class should only inherit one class. A Mixin is another class that can be inherited from allwoing for a class to inherit more classes essentially. 
from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    UserPassesTestMixin
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

class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title", "subtitle", "author", "body"]

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "posts/edit.html"
    model = Post
    fields = ["title", "subtitle", "author", "body"] # Fields will be showed on the page
    # Test for UserPassesTestMixin
    def test_func(self):
        post_obj = self.get_object()
        return post_obj.author == self.request.user

# delete view for details

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    # success_url ="/posts" # You can specify success urlurl to redirect after successfully
    template_name = "posts/confirm_delete.html" # deleting object
    success_url = reverse_lazy("list")
    # Test for UserPassesTestMixin
    def test_func(self):
        post_obj = self.get_object()
        return post_obj.author == self.request.user
