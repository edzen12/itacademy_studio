from django.contrib import admin

from apps.blog.models import Posts

class AdminPosts(admin.ModelAdmin):
    save_on_top = True
    list_display = ['name', 'tag']

admin.site.register(Posts, AdminPosts)
