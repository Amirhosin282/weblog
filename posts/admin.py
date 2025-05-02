from django.contrib import admin
from .models import Post, Comment

class CommentAdminInLin(admin.StackedInline):
    model = Comment
    fields =  ['titel', 'post', 'user_name','id', 'text']
    extra = 0

class PostAdmin (admin.ModelAdmin):
    list_display = ['titel', 'id', 'user_name', 'is_enable', 'create_date']
    inlines = CommentAdminInLin, 

class CommentAdmin(admin.ModelAdmin):
    list_display = ['titel', 'user_name','id', 'post', 'submit_date']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)