from django.shortcuts import render

from .models import Post


def home(request):
    return render(request, "home.html")

def test_view(request):
    return render(request, "test.html")

def post_list_view(request):
    posts = Post.objects.all()
    return render(request, "post_list.html", context={"posts": posts})

def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, "post_detail.html", context={"posts": posts})