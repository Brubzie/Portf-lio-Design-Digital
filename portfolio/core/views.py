from django.shortcuts import render
from django.views import View
from .models import UsuarioModel


class IndexView(View):
    template_name = "index.html"

    def get(self, request):
        return render(request, self.template_name)


class CadastroView(View):
    template_name = "cadastro.html"

    def get(self, request):
        return render(request, self.template_name)


class LoginView(View):
    template_name = "login.html"

    def get(self, request):
        return render(request, self.template_name)


def usuarios(request):
    novo_usuario = UsuarioModel()
    novo_usuario.nome = request.POST.get("nome")
    novo_usuario.idade = request.POST.get("idade")
