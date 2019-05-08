from django.db import models

class curso(models.Model):
    nomecurso = models.CharField("nomecurso", max_length=90)
    horas = models.CharField("horas", max_length=90)
    descrição = models.CharField("descrição", max_length=1000)
    sigal = models.CharField("sigal", max_length=3)
    def __str__(self):
        return self.nome



