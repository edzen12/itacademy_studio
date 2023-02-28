from django.contrib import admin
from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static
from apps.contact.views import contact


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.project.urls')),
    path('contact/', contact, name='contacts'),
    path('blog/', include('apps.blog.urls')),
    path('about/', include('apps.about.urls')),
    path('service/', include('apps.service.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
