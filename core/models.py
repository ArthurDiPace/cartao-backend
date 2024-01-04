from django.db import models

class Cartoes(models.Model):
    numero = models.CharField(max_length=20,null=True, blank=True)
    nome = models.CharField(max_length=29, null=True, blank=True)
    data = models.DateField(null=True, blank=True)
    lote = models.CharField(max_length=15, null=True, blank=True)
    qtd_registro = models.CharField(max_length=10, null=True, blank=True)
    identificador_linha = models.CharField(max_length=200, null=True, blank=True)
    numero_lote = models.CharField(max_length=20, null=True, blank=True)
   