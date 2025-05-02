
from django.contrib import admin
from django.urls import path
from users.views import login, signUp, contact
from homepage.views import posts, PostsDeatils, contact, about, all_posts

urlpatterns = [
    path ('admin458458/', admin.site.urls),
    path ('login/', login),
    path ('', posts),
    path ("post/<int:post_id>/", PostsDeatils),
    path ('login/', login),
    path ('signup/', signUp),
    path ('contact/', contact),
    path ('about/', about),
    path ('posts/', all_posts),
    path('contact/', contact, name='contact'),
    path('contact/processform/', contact, name='process_contact_form')
]