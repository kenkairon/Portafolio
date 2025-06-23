from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm  # Importamos el formulario

# Listar posts
def post_list(request):
    posts = Post.objects.all().order_by('-date_published')
    return render(request, 'blog/post_list.html', {'posts': posts})

# Detalle de un post
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})