"""
URL configuration for sitio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
"""
from django.urls import path, include
from .views import Arriendos, login, addproduc, admpagregar, adm, admpedidos, editarprod, registro
""" from .views import """

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #URLS DE APLICACION
    path('',Arriendos,name='Arriendos'),
    path('addproduc/',addproduc, name='addproduc'),
    path('adm/',adm, name='adm'),
    path('admpagregar/',admpagregar, name='admpagregar'),
    path('admpedidos/',admpedidos, name='admpedidos'),
    path('editarprod/',editarprod, name='editarprod'),
    path('login/',login, name='login'),
    path('registro/',registro, name='registro'),




]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)