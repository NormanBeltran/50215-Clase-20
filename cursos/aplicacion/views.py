from django.shortcuts import render
from .models import *

# Copyright Norman Beltran

def home(request):
    return render(request, "aplicacion/index.html") 

def cursos(request):
    contexto = {'cursos': Curso.objects.all()}
    return render(request, "aplicacion/cursos.html", contexto) 

def profesores(request):
    return render(request, "aplicacion/profesores.html") 

def estudiantes(request):
    return render(request, "aplicacion/estudiantes.html") 

def entregables(request):
    return render(request, "aplicacion/entregables.html") 

#________________________________________ Adicionales
def acerca(request):
    return render(request, "aplicacion/acerca.html") 