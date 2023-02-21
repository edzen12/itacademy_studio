from django.urls import path
from apps.project.views import homepage

urlpatterns = [
    path('', homepage, name='homepage'),
]