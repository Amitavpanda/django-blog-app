from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditPostForm
from django.urls import reverse_lazy

# Create your views here.
# def home(request):
#     return render(request, './theblog/home.html', {})
from .models import Post


class HomeView(ListView):
    model = Post
    template_name = './theblog/home.html'
    ordering = ['-post_date']


class ArticleDetailsView(DetailView):
    model = Post
    template_name = './theblog/article_details.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = './theblog/add_post.html'


class EditPostView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = './theblog/update_post.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = './theblog/delete_post.html'
    success_url = reverse_lazy('home')
