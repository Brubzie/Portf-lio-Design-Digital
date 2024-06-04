from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.IndexView.as_view(), name="index"),
    path("usuario/cadastro", views.CadastroView.as_view(), name="cadastro"),
    path("usuario/login", views.LoginView.as_view(), name="login"),
]