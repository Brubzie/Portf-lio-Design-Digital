from django import forms
from .models import UsuarioModel
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


class UsuarioForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Entrar", css_class="btn btn-primary"))

    nome = forms.CharField(
        label="Nome completo",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Nome completo",
                "type": "text",
            }
        ),
    )

    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Email",
                "type": "email",
            }
        ),
    )

    senha = forms.CharField(
        label="Senha",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Senha",
                "type": "password",
            }
        ),
    )

    class Meta:
        model = UsuarioModel
        fields = [
            "nome",
            "email",
            "senha",
        ]  # Definir os campos do modelo a serem utilizados


class LoginForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=100)
    senha = forms.CharField(label="Senha", widget=forms.PasswordInput())
