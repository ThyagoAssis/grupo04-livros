from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import  reverse_lazy
# Create your views here.
from .models import Livros

class LivrosListView(ListView):
    model = Livros

class LivrosCreateView(CreateView):
    model = Livros
    fields = ['nome','imagem','editora','autor','publicado_em']
    success_url = reverse_lazy('livros_list')


class LivrosLancamento(ListView):
    model= Livros
    template_name = 'livros/livros_lan.html'

class LivrosUpdateView(UpdateView):
    model = Livros
    fields = ['nome', 'imagem', 'editora', 'autor', 'publicado_em']
    template_name = 'livros/livros_form.html'
    success_url = reverse_lazy('livros_list')

class LivrosDeleteView(DeleteView):
    model = Livros
    template_name = 'livros/livros_delete.html'
    success_url = reverse_lazy('livros_list')