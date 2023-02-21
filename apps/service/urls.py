from django.urls import path
from apps.service.views import service_page_view

urlpatterns = [ 
    path('', service_page_view, name='service_page'),
]