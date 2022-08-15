from django.db import models
from django.contrib.auth import get_user_model

class Lingua(models.Model):
    codigo = models.CharField(max_length=5)
    nome = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.codigo+ " - "+self.nome
    

class Fonte(models.Model):
    organizacao = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    co_autor = models.TextField(null=True)
    data_criacao = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Area(models.Model):
    nome = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.nome
    
class Area_Especifica(models.Model):
    descricao = models.CharField(max_length=255)
    curso = models.ForeignKey('Curso',on_delete=models.CASCADE, related_name="cursos")   
    area = models.ForeignKey('Area',on_delete=models.CASCADE,related_name="areas")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.descricao  

class Formato(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    create_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.nome
    

class Licenca(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='uploads/')
    create_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.nome

class Recurso(models.Model):
    titulo = models.CharField(max_length=255) 
    sub_titulo = models.CharField(max_length=500) 
    descricao = models.TextField()
    palavras_chave = models.TextField()
    duracao = models.IntegerField()
    extencao = models.CharField(max_length=255)
    link = models.TextField()
    isactivo = models.IntegerField(default=0)
    ficheiro = models.FileField(upload_to='recurso/%Y/%m/%d', null= True)
    lingua = models.ForeignKey('Lingua',on_delete=models.CASCADE,related_name="linguas")  
    area_especifica = models.ForeignKey('Area_Especifica',on_delete=models.CASCADE, related_name="area_especifica")  
    fonte = models.ForeignKey('Fonte',on_delete=models.CASCADE,related_name="fontes")  
    formato = models.ForeignKey('Formato',on_delete=models.CASCADE, related_name="formatos")  
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE, related_name="publicador")  
    licenca = models.ForeignKey('Licenca',null=True,on_delete=models.CASCADE, related_name="licencas")  
    created_at = models.DateTimeField( auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.titulo

class Contributo(models.Model):
    recurso = models.ForeignKey('Recurso',on_delete=models.CASCADE, related_name="recurso_contributo") 
    contribuicao = models.ForeignKey('Recurso',on_delete=models.CASCADE, related_name="recurso_contribuicao")
    created_at = models.DateTimeField( auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)