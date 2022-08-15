from django.db import models
from django.contrib.auth import get_user_model
from recursos.models import Recurso

class Classificacao(models.Model):
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE, related_name="user_classificacoes")  
    recurso = models.ForeignKey('recursos.Recurso',on_delete=models.CASCADE, related_name="recursos_classificacoes")  
    created_at = models.DateTimeField( auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Comentario(models.Model):
    comentario = models.TextField()
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE, related_name="user_comentarios")  
    recurso = models.ForeignKey('recursos.Recurso',on_delete=models.CASCADE, related_name="recursos_comentarios")  
    created_at = models.DateTimeField( auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
