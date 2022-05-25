from time import timezone
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.blogapp.forms import PostForm, CommentsForm
from django.urls import reverse_lazy
from blogapp.models import Post, Comments
from django.views.generic import (TemplateView,CreateView,
                                  ListView,UpdateView,
                                  DetailView )

# Create your views here.

class AboutView(TemplateView):
    template_name ='about.html'

class PostListView(ListView): #This is the Home Page
    model=Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-publushed_date')

class PostDetailView(DetailView):
    model=Post

class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blogapp/post_detail.html'
    form_class = PostForm
    model=Post

class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blogapp/post_detail.html'
    form_class = PostForm
    model=Post

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model=Post
    success_url=reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'blogapp/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')





