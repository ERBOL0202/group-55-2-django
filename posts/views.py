from django.shortcuts import render, HttpResponse, redirect

from posts.models import Post
from posts.forms import PostForm, PostUpdatedForm, SearchForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView

"""
posts = [post1, post2, post3, post4, post5, post6, post7, post8, post9, post10, post11, post12, post13, post14, post15, post16, post17, post18, post19, post20]
limit = 3
page = 5
max_pages = len(posts)/limit
if round(max_pages) < max_pages:
    max_pages += 1
else:
    max_pages = round(max_pages)
start = (page-1) * limit
end = page * limit

"""

def home_page_view(request):
    if request.method == "GET":
        return render(request, "home.html")

def test_view(request):
    if request.method == "GET":
        return render(request, "test.html")
    
@login_required(login_url="/login")
def post_list_view(request):
    limit = 3
    if request.method == "GET":
        posts = Post.objects.exclude(author=request.user)
        form = SearchForm()
        print(request.GET)
        q = request.GET.get("q")
        category_id_value = request.GET.get("category_id")
        tag_ids = request.GET.getlist("tag_ids")
        ordering = request.GET.get("ordering")
        page = int(request.GET.get("page", 1))
        if q:
            posts = posts.filter(Q(title__icontains=q) | Q(content__icontains=q))
        if category_id_value:
            posts = posts.filter(category_id=category_id_value)
        if tag_ids:
            posts = posts.filter(tags__id__in=tag_ids).distinct()
        if ordering:
            posts = posts.order_by(ordering)
        if page:
            max_pages = posts.count() / limit
            if round(max_pages) < max_pages:
                max_pages = round(max_pages) + 1
                else:
                max_pages = round(max_pages)
            start = (page - 1) * limit
            end = page * limit
            posts = posts[start:end]

        return render(request, "post_list.html", context={"posts": posts, "form": form, "max_pages": range(1, max_pages + 1)})
    
@login_required(login_url="/login")
def post_detail_view(request, post_id):
    if request.method == "GET":
        post = Post.objects.get(id=post_id)
        return render(request, "post_detail.html", context={"posts": posts})
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect("post_detail", post_id=post.id)
    else:
        form = CommentForm()
    return render(request, "post_detail.html", context={"posts": posts, "comment":comment})
    
class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = "post"
    pk_url_kwarg = "post_id"

@login_required(login_url="/login")
def post_create_view(request):
    if request.method == "GET":
        form = PostForm()
        return render(request, "post/post_create.html", context=("form": form))
    if request.method == "POST":
        form = PostForm(request.Post, request.FILES)
        if not form.is_valid():
            return render(request, "post/post_create.html", context=("form": form))
        else:
            title = form.cleaned_data.get("title")
            content = form.cleaned_data.get("content")
            image = form.cleaned_data.get("image")
            Post.objects.create(title=title, content=content, image=image)
        return redirect("/posts")

class PostCreateView(CreateView):
    model = Post
    template_name =  "post/post_create.html"
    form_class = PostForm
    success_url = "/posts/class/"

def post_update_view(request, post_id):
    post = Post.objects.filter(id=post_id).first()
    if not post:
        return HttpResponse("Post not found")
    if request.method == "GET":
        form = PostUpdatedForm(instance=post)
        return render(request, "posts/post_update.html", context={"form":form, "post":post})
    if request.method == "POST":
        post = PostUpdatedForm(request.POST, request.FILES, instance=post)
        if not form.is_valid():
            return render(request, "posts/post_update.html", context={"form":form})
        elif form.is_valid():
            form.save()
            return redirect("profile")
        
class PostUpdateView(UpdateView):
    model = Post
    template_name = "posts/post_update.html"
    form_class = PostForm
    success_url = "/posts/class/"