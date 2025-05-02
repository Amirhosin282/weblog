from django.db import models

class Users(models.Model):
    name = models.CharField(max_length= 50)
    last_name = models.CharField(max_length= 50)
    user_name = models.CharField(max_length= 35)
    bio = models.TextField(max_length= 500, null= True, blank= True)
    join_date = models.DateTimeField(auto_now= True)
    email_addr = models.EmailField(max_length= 100)
    phone_number = models.CharField(max_length= 15)
    password = models.CharField(max_length= 20)
    image = models.ImageField(upload_to='homepage/static/assets/img/profiles', blank=True, null=True)
    
    def __str__(self):
        return self.user_name

class Messeage(models.Model):
    name = models.CharField(max_length= 50)
    email_addr = models.CharField(max_length= 100)
    phone_number = models.CharField(max_length= 15)
    message = models.TextField(max_length= 1000)
    create_date = models.DateTimeField(auto_now= True)