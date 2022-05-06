from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class PostListView(ListView):
    template_name = 'posts/list.html'
    model = Post


class PostDetailView(DetailView):
    template_name = 'posts/detail.html'
    model = Post 

class PostCreateView(LoginRequiredMixin, CreateView):
        template_name = 'posts/new.html'
        model = Post 
        fields = ['title', 'author','body']

class PostUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'posts/edit.html'
    model = Post
    fields = ['title', 'body']


class PostDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'posts/delete.html'
    model = Post
    success_url = reverse_lazy('post_list')

