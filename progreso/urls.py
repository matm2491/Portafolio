from django.urls import path
from . import views

urlpatterns = [

    path('comentarios', views.comment, name = 'comment'),
    path('formulario', views.forms_user, name = 'forms'),
    
]