from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('core.urls')),
    path("admin/", admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('tools/', include('tools.urls')),
    path('borrow/', include('borrow.urls')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)