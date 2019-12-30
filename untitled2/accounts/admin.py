from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import BlogUser

class BlogUserAdmin(UserAdmin):
    list_display = ('id', 'nickname', 'username', 'email', 'last_login', 'date_joined', 'source')
    list_display_links = ('id', 'username')
    ordering = ('-id',)
    
    
admin.site.register(BlogUser, BlogUserAdmin)
