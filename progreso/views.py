from django.shortcuts import render, redirect
from .models import Date
from .forms import CommentsUsers

# Create your views here.


def comment(request):

    comentarios = Date.objects.all()

    return render(request, 'progreso/comment.html', {"comentarios": comentarios})

def forms_user(request):
    users_form= CommentsUsers()

    if request.method=='POST':
        users_form=CommentsUsers(data=request.POST)
        if users_form.is_valid():
            name=request.POST.get('name')
            last_name=request.POST.get('last_name')
            title=request.POST.get('title')
            comment=request.POST.get('comment')
            carga=Date.objects.create(name=name, last_name=last_name,title=title,comments=comment)

            return redirect('/progresocomentarios?valido')

    return render(request, 'progreso/forms_commen.html', {'formulario':users_form})