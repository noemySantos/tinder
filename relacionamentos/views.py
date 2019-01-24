from django.shortcuts import render
from django.http import HttpResponse
from . models import Usuario

def home(request):
    return render(request, 'home.html', {})

def usuario_list(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuario/list.html', {'usuarios':usuarios})

def usuario_show(request, usuario_id):
    usuario = Usuario.objects.get(pk=usuario_id)
    return render(request, 'usuario/show.html', {'usuario':usuario})
