from django.shortcuts import render
from django.http import HttpResponse
from.models import Post, Comment

# def Posts(requests):
#     post_list = Post.objects.all()
#     post_dict = {'posts': post_list}
#     return render (requests, "posts.html", context = post_dict)

# def PostsDeatils(requests, post_id):
#     post = Post.objects.get(pk = post_id)
#     comment = Comment.objects.filter(post = post)
    
#     post_dict = {
#                     'posts' : post,
#                     'comments' : comment
#                  }
#     return render (requests, 'postdetail.html', context= post_dict)
