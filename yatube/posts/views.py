from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Group
from .forms import PostForm

LIMIT_POSTS = 10
LIMIT_LIST = 10


def index(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, LIMIT_LIST)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    posts = Post.objects.select_related()[:LIMIT_POSTS]
    context = {
        'page_obj': page_obj,
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, LIMIT_LIST)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:LIMIT_POSTS]
    context = {
        'page_obj': page_obj,
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, LIMIT_LIST)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, LIMIT_LIST)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/post_detail.html', context)


def post_create(request):
    form = PostForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('posts:profile', request.user.username)
        return render(request, 'posts/create_post.html', {'form': form})
    form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})


def post_edit(request):
    form = PostForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('posts:profile', request.user.username)
        return render(request, 'posts/create_post.html', {'form': form})
    form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})
