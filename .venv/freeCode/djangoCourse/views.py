from django.shortcuts import render
from django.template import loader
from .models import Course,Professor
from django.http import HttpResponse

def index(request):
    lista_cursos = Course.objects.all()
    template = loader.get_template("index.html")
    context:{
        "lista de cursos atualizada":lista_cursos
    }
    #return HttpResponse(template.render(context,request))
    return render(request,"index.html",context)


def pagCurso(request,course_id):
    template = loader.get_template("djangoC.html")
    contexto={
        "curso":Course.objects.get(pk=course_id)
    }
    return render(request,'djangoC.html',contexto)

def professor(request, Professor_id):
    response = "Você está vendo o professor %s"
    return HttpResponse(response % Professor_id)

