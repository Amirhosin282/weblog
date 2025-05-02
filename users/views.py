from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from django.http import HttpResponse
from users.models import Users

def login(requst):
    return render(requst, 'login.html')

def signUp(requests):
    return render (requests, 'signup.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'پیام شما با موفقیت ارسال شد!')
            return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})