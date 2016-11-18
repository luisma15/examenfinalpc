from django.shortcuts import render
from .templates.blib.forms import PostForm

# Create your views here.

def listarp(request):
    return render(request, 'blib/listarp.html', {})

def post_new(request):
    form = PostForm()
    return render(request, 'blib/post_edit.html', {'form': form})
