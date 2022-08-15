from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages

from django.db import transaction
from django.urls import reverse
import os

from .models import *

# Create your views here.
def home(request):
    return render(request,'home.html')

def recursos_form(request):
    licencas = Licenca.objects.all()
    linguas = Lingua.objects.all()
    areas = Area_Especifica.objects.all()
    formatos = Formato.objects.all()
    return render(request,'recursos/recursos_form.html',{'licencas':licencas, 'linguas':linguas,'areas':areas,'formatos':formatos})

def licencasCC(request):
    licencas = Licenca.objects.all()
    return render(request,'licencas/licencasCC.html',{'licencas':licencas})

def recursos_store(request):
    try:
        if request.method == "POST":
            titulo = request.POST.get('titulo', None)
            sub_titulo = request.POST.get('subtitulo', None)
            descricao = request.POST.get('descricao', None)
            palavras_chave = request.POST.get('palavras_chave', None)
            link = request.POST.get('link', None)
            area = request.POST.get('area', None)
            file = request.FILES['file']
            extencao = os.path.splitext(file.name)[1]
            organizacao = request.POST.get('organizacao', None)
            autor = request.POST.get('autor', None)
            co_autor = request.POST.get('coautor', None)
            criacao = request.POST.get('criacao', None)
            lingua = request.POST.get('lingua', None)
            licenca = request.POST.get('licenca', None)
            formato = request.POST.get('formato', None)
            with transaction.atomic():
                fonte=Fonte.objects.create(
                organizacao=organizacao, 
                autor = autor,co_autor = co_autor,
                data_criacao=criacao
            )
                recurso = Recurso.objects.create(
                titulo = titulo,
                sub_titulo = sub_titulo,
                descricao = descricao,
                palavras_chave = palavras_chave,
                duracao = 0,
                extencao = extencao,
                link = link,
                ficheiro = file,
                fonte = fonte,
                lingua = Lingua.objects.get(pk=lingua),
                area_especifica = Area_Especifica.objects.get(pk=area),
                
                formato = Formato.objects.get(pk=formato),
                user = request.user,
                licenca = Licenca.objects.get(pk=licenca)
            )
                messages.success(request, "O Recurso Educacional Aberto "+ recurso.titulo + " foi gravado com sucesso!") 

                return HttpResponseRedirect(reverse('recursos.form'))
    except Exception as ex:
        print(ex)
        transaction.rollback()
        messages.error(request, "O Recurso Educacional Aberto "+ recurso.titulo + " não foi gravado!")
        return HttpResponseRedirect(reverse('recursos.form'))
    else:
        return HttpResponseRedirect(reverse('recursos.form'))


def recursos_all(request, mensagem='None'):
    recursos = Recurso.objects.all()
    return render(request,'recursos/recursos_all.html',{'recursos':recursos,'mensagens': mensagem})
    