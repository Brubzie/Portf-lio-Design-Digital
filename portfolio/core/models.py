from django.db import models


class UsuarioModel(models.Model):
    nome = models.TextField(
        verbose_name="Nome", max_length=100, null=False, blank=False
    )
    email = models.EmailField(verbose_name="Email", null=False, blank=False)
    senha = models.TextField(verbose_name="Senha", null=False, blank=False)

    def __str__(self):
        """Devolve uma representação em string do modelo."""
        return self.nome

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ["nome"]
