from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {"posts": posts})


# View Details
def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {"post": post})


# New Post
class PostCreateView(CreateView):
    model = Post
    template_name= 'blog/post_form.html'
    fields = ["title", "artist", "banner"]
    success_url= reverse_lazy("blog:home")


# Update Post
class PostUpdateView(UpdateView):
    model = Post
    template_name= 'blog/post_edit.html'
    fields = ["title", "artist", "banner"]
    success_url = reverse_lazy("blog:home")


# Delete 
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy("blog:home")
