from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('work', views.work, name= 'work'),
    
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)