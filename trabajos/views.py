from django.shortcuts import render
from .models import Work

# Create your views here.


def work(request):

    trabajos = Work.objects.all()

    return render(request, 'trabajos/trabajos.html', {'trabajos':trabajos})