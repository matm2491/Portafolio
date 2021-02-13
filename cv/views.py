from django.shortcuts import render


# Create your views here.


def index(request):
    
    return render(request, 'cv/index.html')



def vitae(request):

    return render(request, 'cv/vitae.html')


def contact(request):

    return render(request, 'cv/contacto.html')






