from django.shortcuts import render
from apps.project.models import Sett
from apps.blog.models import Posts

def blog_page_view(request):
    setting = Sett.objects.latest('id')   
    posts_others = Posts.objects.filter(tag='Others')
    posts_therd = Posts.objects.filter(tag='Therd')
    name_page = 'Блог'
    context = {
        'setting':setting,
        'posts_others':posts_others,  
        'posts_therd':posts_therd,  
        'name_page':name_page, 
    }
    return render(request, 'page/blog.html', context)
