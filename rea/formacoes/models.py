from tkinter import CASCADE
from django.db import models
from django.contrib.auth import get_user_model
from recursos.models import *


class Formacao(models.Model):
    nome = models.CharField(max_length=500)
    descricao = models.TextField()
    formador = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,related_name="formacao_formador")
    area_especifica = models.ForeignKey('recursos.Area_Especifica', on_delete=models.CASCADE, related_name="assunto_formacao")
    imagem = models.ImageField(upload_to='capas/', null = True)
    created_at = models.DateTimeField( auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.nome

class Formacao_Recurso(models.Model):
    descricao = models.TextField()
    formacao = models.ForeignKey('Formacao', on_delete=models.CASCADE,related_name="formacoes_recurso")
    recurso = models.ForeignKey('recursos.Recurso',on_delete=models.CASCADE, related_name="formacoes_recurso")  
    isapoio = models.IntegerField(default=0)
    created_at = models.DateTimeField( auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Inscrito(models.Model):
    formando = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,related_name="formando")
    formacao = models.ForeignKey('Formacao', on_delete=models.CASCADE)
    created_at = models.DateTimeField( auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

