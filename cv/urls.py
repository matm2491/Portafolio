from django.urls import path
from progreso.urls import views
from . import views





urlpatterns = [

    path('', views.index, name = 'index'),
    path('vitae', views.vitae, name = 'vitae'),
    path('contacto', views.contact, name='contact')
    
    
]