from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from .models import Post

# Create your views here.
class PostListView(ListView):
    queryset = Post.objects.all()
class PostCreateView(CreateView):
    queryset = Post.objects.all()
    model = Post

    fields = “__all__”

    success_url  = reverse_lazy(“blog:all”)
class PostDetailView(DetailView):
    queryset = Post.objects.all()
    model = Post

    fields = “__all__”

    success_url  = reverse_lazy(“blog:all”)
class PostDeleteView(DeleteView):
    queryset = Post.objects.all()
    model = Post

    fields = “__all__”

    success_url  = reverse_lazy(“blog:all”)