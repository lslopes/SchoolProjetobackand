from django.db import models


class usuarios(models.Model):
    nomeuser = models.CharField("nome", max_length=90)
    senha = models.CharField("especialidades", max_length=90)
    def __str__(self):
            return self.nome

