from django.db import models
from django.contrib.auth import get_user_model
from recursos.models import Recurso
from recursos.models import Area_Especifica

class Podcast(models.Model):
    nome = models.CharField(max_length=500)
    descricao = models.TextField()
    assunto = models.ForeignKey('recursos.Area_Especifica', on_delete=models.CASCADE,related_name="assunto_podcast")
    criador = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,related_name="criador_podcast")
    created_at = models.DateTimeField( auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Episodio(models.Model):
    nome = models.CharField(max_length=500)
    descricao = models.TextField()
    numero = models.IntegerField(default=1)
    recurso = models.ForeignKey('recursos.Recurso',on_delete=models.CASCADE, related_name="episodio_podcast")  
    podcast = models.ForeignKey('Podcast',on_delete=models.CASCADE, related_name="episodio_podcast")  
    created_at = models.DateTimeField( auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Subscrito(models.Model):
    inscrito = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,related_name="inscrito_podcast")
    podcast = models.ForeignKey('Podcast',on_delete=models.CASCADE, related_name="inscrito_podcast")  
    created_at = models.DateTimeField( auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
        

