"""rea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, register_converter
from formacoes import views as formacoes_view
from recursos import views as recursos_view

from django.conf import settings 
from django.conf.urls.static import static 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',recursos_view.home, name='home'),
    path('licencas/cc',recursos_view.licencasCC, name='licencas.all'),
    path('recursos/carregar',recursos_view.recursos_form, name='recursos.form'),
    path('recursos/gravar',recursos_view.recursos_store, name='recursos.store'),
    path('recursos/disponiveis',recursos_view.recursos_all, name='recursos.all'),
    path('formacoes/disponiveis',formacoes_view.formacoes_all, name='formacoes.all'),
    path('formacoes/carregar',formacoes_view.formacoes_form, name='formacoes.form'),
    path('formacoes/gravar',formacoes_view.formacoes_store, name='formacoes.store'),
    path('formacoes/detalhes/<int:codigo>/<int:video>', formacoes_view.teste,name='formacoes.detalhes'),
    path('formacoes/add/aula/<int:codigo>', formacoes_view.formacoes_add_aula,name='formacoes.add'),
    path('formacoes/aula/gravar',formacoes_view.formacao_add_recurso, name='formacoes.add.store'),
     
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)