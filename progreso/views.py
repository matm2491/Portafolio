from django.shortcuts import render
from .models import Date

# Create your views here.


def comment(request):

    comentarios = Date.objects.all()

    return render(request, 'progreso/comment.html', {"comentarios": comentarios})