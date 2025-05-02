from django.db import models
from users.models import Users
import datetime

class Post(models.Model):
    titel = models.CharField(max_length= 50)
    text = models.TextField(max_length= 80000)
    user_name = models.ForeignKey(Users, on_delete= models.DO_NOTHING)
    is_enable = models.BooleanField(default= False)
    publish_date = models.DateTimeField(default= datetime.datetime.today())
    update_date = models.DateTimeField(auto_now= True)
    create_date = models.DateTimeField(auto_now= True)
    pic = models.ImageField(upload_to= "homepage/static/assets/img", blank= True, null= True)
    pic_info = models.TextField(max_length= 150, blank= True, null= True)

    def __str__(self):
        return self.titel

class Comment(models.Model):
    titel = models.CharField(max_length= 80)
    post = models.ForeignKey(Post, on_delete= models.DO_NOTHING)
    user_name = models.ForeignKey(Users, on_delete= models.DO_NOTHING)
    text = models.TextField(max_length= 800)
    submit_date = models.DateTimeField(auto_now= True)
    
    def __str__(self):
        return f'comment numb : {self.id} / to {self.post}'