"""crud_biblioteca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from crud_biblioteca.views import pages, produtos,categorias

urlpatterns = [
    path('', pages.home, name='home'),
    path('produtos', produtos.lista, name='produtos.lista'),
    path('produtos/novo', produtos.novo, name='produtos.novo'),
    path('produtos/editar/<id>', produtos.editar, name='produtos.editar'),
    path('produtos/excluir/<id>', produtos.excluir, name='produtos.excluir'),
    
    path('categorias', categorias.lista, name='categorias.lista'),
    path('categorias/novo', categorias.novo, name='categorias.novo'),
    path('categorias/editar/<id>', categorias.editar, name='categorias.editar'),
    path('categorias/excluir/<id>', categorias.excluir, name='categorias.excluir')
]
