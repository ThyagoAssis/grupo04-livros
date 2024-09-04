from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import  reverse_lazy
# Create your views here.
from .models import Livros

#Cptura de sessoes
from django.views import View
from django.shortcuts import render,redirect

class LivrosListView(ListView):
    model = Livros

    def get(self, request, *args, **kwargs):
        # Verifica se a sessão tem 'nome_usuario'
        if 'nome_usuario' not in request.session:
            return redirect('livros_sessao')  # Redireciona para a página de login se a sessão não estiver ativa

        # Se a sessão estiver ativa, continue com a lógica padrão da ListView
        return super().get(request, *args, **kwargs)

class LivrosCreateView(CreateView):
    model = Livros

    def get(self, request, *args, **kwargs):
        # Verifica se a sessão tem 'nome_usuario'
        if 'nome_usuario' not in request.session:
            return redirect('livros_sessao')  # Redireciona para a página de login se a sessão não estiver ativa

        # Se a sessão estiver ativa, continue com a lógica padrão da ListView
        return super().get(request, *args, **kwargs)

    fields = ['nome','imagem','editora','autor','publicado_em']
    success_url = reverse_lazy('livros_list')


class LivrosLancamento(ListView):
    model= Livros

    def get(self, request, *args, **kwargs):
        # Verifica se a sessão tem 'nome_usuario'
        if 'nome_usuario' not in request.session:
            return redirect('livros_sessao')  # Redireciona para a página de login se a sessão não estiver ativa

        # Se a sessão estiver ativa, continue com a lógica padrão da ListView
        return super().get(request, *args, **kwargs)

    template_name = 'livros/livros_lan.html'

class LivrosUpdateView(UpdateView):
    model = Livros

    def get(self, request, *args, **kwargs):
        # Verifica se a sessão tem 'nome_usuario'
        if 'nome_usuario' not in request.session:
            return redirect('livros_sessao')  # Redireciona para a página de login se a sessão não estiver ativa

        # Se a sessão estiver ativa, continue com a lógica padrão da ListView
        return super().get(request, *args, **kwargs)

    fields = ['nome', 'imagem', 'editora', 'autor', 'publicado_em']
    template_name = 'livros/livros_form.html'
    success_url = reverse_lazy('livros_list')

class LivrosDeleteView(DeleteView):
    model = Livros

    def get(self, request, *args, **kwargs):
        # Verifica se a sessão tem 'nome_usuario'
        if 'nome_usuario' not in request.session:
            return redirect('livros_sessao')  # Redireciona para a página de login se a sessão não estiver ativa

        # Se a sessão estiver ativa, continue com a lógica padrão da ListView
        return super().get(request, *args, **kwargs)

    template_name = 'livros/livros_delete.html'
    success_url = reverse_lazy('livros_list')


##Capturando sessões
class SolicitarDadosView(View):

    def get(self, request):
        return render(request, 'section/section.html')

    def post(self, request):
        nome_usuario = request.POST.get('nome_usuario')
        email = request.POST.get('email')

        # Armazenando os dados na sessão
        request.session['nome_usuario'] = nome_usuario
        request.session['email'] = email

        return redirect('livros_list')


##Encerrar a sessao
class EncerrarSessaoView(View):
    def get(self, request):
        request.session.flush()  # Remove todos os dados da sessão e exclui a sessão
        return redirect('/')  # Redireciona para a página inicial ou qualquer outra página