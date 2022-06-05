from django.shortcuts import render
from django.views.generic import ListView, DetailView, edit
from django.urls import reverse_lazy
from .models import Post
# Create your views here.


class PostListView(ListView):
    model = Post
    template_name = 'home.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(edit.CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']


class BlogUpdateView(edit.UpdateView):
    model = Post
    template_name = 'edit_post.html'
    fields = ['title', 'body']


class BlogDeleteView(edit.DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')