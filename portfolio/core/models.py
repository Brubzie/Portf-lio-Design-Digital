from django.db import models

class UsuarioModel(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=100)
    idade = models.IntegerField()

    def __str__(self):
        """Devolve uma representação em string do modelo."""
        return self.nome

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
    