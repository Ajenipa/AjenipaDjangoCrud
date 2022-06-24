from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from .models import Post
# Create your views here.
class PostListView(ListView):
    template_name = "blog/post_list.html"
    model = Post
class PostCreateView(CreateView):
    template_name = "blog/post_form.html"
    model = Post
    fields = '__all__'
    success_url  = reverse_lazy('blog:all')
class PostDetailView(DetailView):
    model = Post
    fields = '__all__'
    success_url  = reverse_lazy('blog:all')
class PostUpdateView(UpdateView):
    model = Post
    fields = '__all__'
    success_url  = reverse_lazy('blog:all')
class PostDeleteView(DeleteView):
    model = Post
    fields = '__all__'
    success_url  = reverse_lazy('blog:all')