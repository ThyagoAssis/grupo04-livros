from django.views.generic import ListView, CreateView
from django.urls import  reverse_lazy
# Create your views here.
from .models import Livros

class LivrosListView(ListView):
    model = Livros

class LivrosCreateView(CreateView):
    model = Livros
    fields = ['nome','imagem','editora','autor','publicado_em']
    success_url = reverse_lazy('livros_list')