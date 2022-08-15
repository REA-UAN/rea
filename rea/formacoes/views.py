import os
from shutil import ExecError
from webbrowser import get
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
import datetime
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.contrib import messages


from django.db import transaction
from django.urls import reverse

def teste(request, codigo, video):
    try:
        reproducao = Formacao_Recurso.objects.get(Q(pk=video),Q(formacao_id = codigo)) 
        aulas = Formacao_Recurso.objects.filter(formacao_id = codigo)
        return render(request,'formacoes/formacoes_detalhes.html',{'materiais':aulas ,'formacao':codigo,'reproducao':reproducao})
    except Exception as ex:
        reproducao = None 
        aulas = Formacao_Recurso.objects.filter(formacao_id = codigo)
        return render(request,'formacoes/formacoes_detalhes.html',{'materiais':aulas ,'formacao':codigo,'reproducao':reproducao})

def formacoes_add_aula(request,codigo):
    formacao = Formacao.objects.get(pk=codigo)
    licencas = Licenca.objects.all()
    linguas = Lingua.objects.all()
    areas = formacao.area_especifica
    formatos = Formato.objects.all()
    return render(request,'formacoes/formacoes_add.html',{'licencas':licencas, 'linguas':linguas,'areas':areas,'formatos':formatos,'formacao':formacao})

def formacoes_form(request):
    areas = Area_Especifica.objects.all()
    return render(request,'formacoes/formacoes_form.html',{'areas':areas})

def formacoes_all(request):
    formacoes = Formacao.objects.all()
    return render(request,'formacoes/formacoes_all.html',{'formacoes':formacoes})




def formacoes_store(request):
    try:
        if request.method == "POST":
            nome = request.POST.get('nome', None)
            descricao = request.POST.get('descricao', None)
            area = request.POST.get('area', None)
            file = request.FILES['file']
            with transaction.atomic():
                Formacao.objects.create(
                nome = nome, 
                descricao = descricao,
                imagem = file,
                formador = request.user,
                area_especifica = Area_Especifica.objects.get(pk=area)   
                )
                
                messages.success(request, "A Formação foi gravada com sucesso!") 

                return HttpResponseRedirect(reverse('formacoes.form'))
    except Exception as ex:
        print(ex)
        transaction.rollback()
        messages.error(request, "A Formação não foi gravada!")
        return HttpResponseRedirect(reverse('formacoes.form'))
    else:
        return HttpResponseRedirect(reverse('formacoes.form'))

def formacao_add_recurso(request):
    formacao_id = request.POST.get('formacao_id', None)
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
            apoio = request.POST.get('apoio', None)
            organizacao = request.POST.get('organizacao', None)
            autor = request.POST.get('autor', None)
            co_autor = request.POST.get('coautor', None)
            criacao = request.POST.get('criacao', None)
            lingua = request.POST.get('lingua', None)
            licenca = request.POST.get('licenca', None)
            formato = request.POST.get('formato', None)
            
            if(apoio == '0'):
                if(extencao != ".mkv" and extencao != ".mp4" and extencao != ".webM"):
                    messages.warning(request, "O Recurso Educacional Aberto Não Possiu a Extenção Ideal!") 
                    return HttpResponseRedirect(reverse('formacoes.add', kwargs={'codigo': formacao_id}) )  
            
            with transaction.atomic():
                fonte=Fonte.objects.create(
                    organizacao=organizacao, 
                    autor = autor,co_autor = co_autor,
                    data_criacao = datetime.datetime.now()
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

                formacao = Formacao_Recurso.objects.create(
                    descricao = titulo,
                    formacao = Formacao.objects.get(pk=formacao_id),
                    recurso = recurso,  
                    isapoio = apoio,
                )
                messages.success(request, "O Recurso Educacional Aberto "+ recurso.titulo + " foi gravado com sucesso!") 

                return HttpResponseRedirect(reverse('formacoes.add', kwargs={'codigo': formacao_id}) )  

    except Exception as ex:
        print(ex)
        transaction.rollback()
        messages.error(request, "O Recurso Educacional Aberto não foi gravado!")
        return HttpResponseRedirect(reverse('formacoes.add', kwargs={'codigo': formacao_id}) )  
    else:
        return HttpResponseRedirect(reverse('formacoes.add', kwargs={'codigo': formacao_id}) )
