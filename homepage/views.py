from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse
from posts.models import Post, Comment
import random

def all_posts(request):
    posts_list = Post.objects.filter(is_enable=True)
    
    sort_by = request.GET.get('sort')
    if sort_by == 'newest':
        posts_list = posts_list.order_by('-create_date')
    elif sort_by == 'oldest':
        posts_list = posts_list.order_by('create_date')
    else:
        posts_list = posts_list.order_by('-create_date')

    paginator = Paginator(posts_list, 9)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    
    context = {'posts': posts}
    
    return render(request, 'all_posts.html', context= context)


def posts(request):
    # Get all enabled post IDs
    enabled_post_ids = Post.objects.filter(is_enable=True).values_list('id', flat=True)
    total_enabled_posts = len(enabled_post_ids)

    # Check if we have enough enabled posts
    if total_enabled_posts < 4:
        return HttpResponse("Not enough enabled posts available", status=400)

    # Select 4 unique random posts from enabled ones
    selected_ids = random.sample(list(enabled_post_ids), 4)
    selected_posts = Post.objects.filter(id__in=selected_ids)
    
    # get a random post
    random_id = int(random.choice(enabled_post_ids))
    random_post = Post.objects.get(pk=random_id)

    # Create context dictionary dynamically
    context = {
        f'post{i+1}': post for i, post in enumerate(selected_posts)
    }
    context['random_post'] = random_post

    return render(request, "index.html", context=context)


# for show comments
def PostsDeatils(requests, post_id):
    number = 1
    post = Post.objects.get(id = post_id)
    comment = Comment.objects.filter(post = post)

    post_pic = post.pic
    post_pic_info = post.pic_info

    if post_pic == None or post_pic == "":
        post_pic = "assets/img/none.png"
        post_pic_info = ""
    else :
        post_pic = str(post_pic).replace("homepage/static/", "").strip()
    
    post_dict = {
                    'posts' : post,
                    'comments' : comment,
                    'pic' : post_pic,
                    'pic_info' : post_pic_info,
                    'number' : number
                 }
    return render (requests, 'post.html', context= post_dict)

def login (requests):
    return render(requests, "login.html")

def contact(requests):
    return render (requests, "contact.html")

def about(requests):
    return render (requests, "about.html")