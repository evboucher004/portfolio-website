from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'portfolio/post_list.html', {'posts': posts})


def index(request):
    return render(request, 'portfolio/index.html')

def imsp(request):
    return render(request, 'portfolio/imsp.html')

def mtg(request):
    return render(request, 'portfolio/mtg.html')

def snhu(request):
    return render(request, 'portfolio/snhu.html')