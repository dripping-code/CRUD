from django.views.generic.edit import CreateView
from django.views.generic.edit import ListView
from django.views.generic.edit import DetailView
from django.views.generic.edit import UpdateView
from django import views
from django.shortcuts import render
from django.urls import reverse_lazy
from zuridjango.flow.blog.models import Post

# Create your views here.
class PostListView(ListView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blod:all")

class PostDetailView(DetailView):
    model = Post

class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy

class PostDeleteView(UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy