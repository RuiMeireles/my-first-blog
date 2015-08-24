from django.shortcuts import render

# Create your views here.

from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from django import template
from django.http import Http404

def post_list(request):
    #posts = Post.objects.all()
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
    #return render(request, 'blog/post_list.html', {})
    
def post_detail(request, pk):
    #post = Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
    
def example(request, id):
    try:
        return render(request, 'blog/example' + id + '.html', {})
    except template.TemplateDoesNotExist:
        raise Http404

