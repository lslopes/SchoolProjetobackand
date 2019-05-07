from django.db import models

class discipilna(models.Model):
    nomediscipilna = models.CharField("nomediscipilna", max_length=90)
    descriçãodis = models.CharField("descrição", max_length=1000)
    def __str__(self):
        return self.nomediscipilna

