"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from livros.views import LivrosCreateView,LivrosListView,LivrosDeleteView,LivrosUpdateView, LivrosLancamento, SolicitarDadosView, EncerrarSessaoView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('livros', LivrosListView.as_view(),name='livros_list'),
    path('cadastro/', LivrosCreateView.as_view(), name='livros_form'),
    path('lançamentos/',LivrosLancamento.as_view(), name='livros_lan'),
    path('edicao/<int:pk>/',LivrosUpdateView.as_view(), name='livros_edicao'),
    path('delete/<int:pk>/',LivrosDeleteView.as_view(), name='livros_delete'),

    path('', SolicitarDadosView.as_view(), name='livros_sessao'),
    path('encerra/', EncerrarSessaoView.as_view(), name='livros_encerra_sessao')
]
