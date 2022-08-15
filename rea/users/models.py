from django.db import models
from django.contrib.auth import get_user_model
from recursos.models import Area
from recursos.models import Recurso
from rea_users.models import *

class Carteira(models.Model):
    dono = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name="carteira_dono")  
    membro = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name="membros_carteira")  
    created_at = models.DateTimeField( auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Comunidade(models.Model):
    nome = models.CharField(max_length=255)
    criador = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)  
    assunto = models.ForeignKey('recursos.Area',on_delete=models.CASCADE,related_name="comunidade_assunto")
    created_at = models.DateTimeField( auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Comunidade_Recurso(models.Model):
    comunidade = models.ForeignKey('Comunidade',on_delete=models.CASCADE)
    recurso = models.ForeignKey('recursos.Recurso',on_delete=models.CASCADE, verbose_name="comunidade_recursos")
    created_at = models.DateTimeField( auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Membro(models.Model):
    comunidade = models.ForeignKey('Comunidade',on_delete=models.CASCADE)
    membro = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)  
    isadmin = models.IntegerField(default=0)
    isactivo = models.IntegerField(default=1)
    ispublica = models.IntegerField(default=1)
    created_at = models.DateTimeField( auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


class Forum(models.Model):
    pergunta = models.CharField(max_length=500)
    descricao = models.TextField()
    criador = models.ForeignKey(get_user_model(),on_delete=models.CASCADE, related_name="criador_forum")  
    created_at = models.DateTimeField( auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Resposta(models.Model):
    resposta = models.ForeignKey("rea_users.Comentario", on_delete=models.CASCADE,related_name="respostas")
    forum = models.ForeignKey("Forum", on_delete=models.CASCADE,related_name="respostas")
    classificao = models.ForeignKey("rea_users.Classificacao", on_delete=models.CASCADE,related_name="respostas")
    created_at = models.DateTimeField( auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)