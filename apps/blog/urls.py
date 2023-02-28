from django.urls import path
from apps.blog.views import blog_page_view

urlpatterns = [ 
    path('', blog_page_view, name='blog_page'),
]