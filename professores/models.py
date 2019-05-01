from django.db import models


class professores(models.Model):
    nome = models.CharField("nome", max_length=90)
    especialidades = models.CharField("especialidades", max_length=90)
    graduacoes = models.CharField("graduacoes", max_length=1000)
    vinculo_dsicipilnas = models.CharField("vinculo_dsicipilnas", max_length=90)
    def __str__(self):
        return self.nome


