from django.urls import path
from apps.project.views import homepage , projects

urlpatterns = [
    path('', homepage, name='home'), 
    path('projects/', projects, name='projects'), 
]