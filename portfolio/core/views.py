from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from .forms import UsuarioForm, LoginForm
from .models import UsuarioModel


class IndexView(View):
    template_name = "index.html"

    def get(self, request):
        return render(request, self.template_name)


class CadastroView(View):
    template_name = "cadastro.html"

    def get(self, request):
        form = UsuarioForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = UsuarioForm(request.POST)
        if form.is_valid():
            nome_completo = form.cleaned_data["nome"]
            email = form.cleaned_data["email"]
            senha = form.cleaned_data["senha"]
            if User.objects.filter(username=email).exists():
                messages.error(
                    request, "Já existe um usuário com este email cadastrado."
                )
                return render(request, self.template_name, {"form": form})

            user = User.objects.create_user(username=email, email=email, password=senha)
            user.first_name = nome_completo
            user.save()
            messages.success(request, "Usuário cadastrado com sucesso.")
            return redirect("login")
        return render(request, self.template_name, {"form": form})


class LoginView(View):
    template_name = "login.html"

    def get(self, request):
        form = LoginForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            senha = form.cleaned_data["senha"]
            user = authenticate(request, username=email, password=senha)
            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                messages.error(request, "Email ou senha incorretos.")

        return render(request, self.template_name, {"form": form})


def LogoutView(request):
    """Faz logout do usuário."""
    logout(request)
    return redirect("index")
