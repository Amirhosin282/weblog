from django.contrib import admin
from .models import Users, Messeage

class UserAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'id','email_addr','phone_number' ,'join_date' ]

class MesseageAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'email_addr', 'phone_number']

admin.site.register(Users, UserAdmin)
admin.site.register(Messeage, MesseageAdmin)