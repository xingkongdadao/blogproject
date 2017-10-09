
from django.shortcuts import render
from blog.models import Post


# Create your views here.

def index(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', locals())
