from django.urls import path
from . import views





urlpatterns = [

    path('', views.index, name = 'index'),
    path('vitae', views.vitae, name = 'vitae'),
]