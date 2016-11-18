from django.shortcuts import render
from .templates.blib.forms import PostForm

# Create your views here.

def listarp(request):
    return render(request, 'blib/listarp.html', {})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, 'blib/post_edit.html', {'form': form})
    else:
        form=PostForm()
    return render(request, 'blib/post_edit.html', {'form': form})


#def post_new(request):
    #if request.method == "POST":
    #    form = PostForm(request.POST)
    #    if form.is_valid():
    #        post = form.save(commit=False)
    #        #post.author = request.user
    #        #post.published_date = timezone.now()
    #        post.save()
    #        return render('blib/post_edit.html', {'form': form})
    #else:
    #    form = PostForm();
    #return render('blib/post_edit.html', {'form': form})
#    form = PostForm()
#    return render(request, 'blib/post_edit.html', {'form': form})
