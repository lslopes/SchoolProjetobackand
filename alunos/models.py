from django.db import models

class alunos(models.Model):
    nome = models.CharField("Nome", max_length=90)
    curso = models.CharField("curso", max_length=90)
    endereço = models.CharField("endereço", max_length=90)
    mensalidade = models.IntegerField("mensalidade")
    def __str__(self):
        return self.nome
