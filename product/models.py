from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Categoria(models.TextChoices):
    ELETRONICOS = "Eletronicos"
    COMIDA = "Comidas"
    CASA = "Casa"
    COZINHA = "Cozinha"
    ROUPAS = "Roupas"
    ESPORTE = "Esporte"
    BRINQUEDOS = "Brinquedos"
    LIVROS = "Livros"

class Produto(models.Model):
    nome = models.CharField(max_length=255, default='', blank=False)
    descricao = models.TextField(max_length=1000, default='', blank=False)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    marca = models.CharField(max_length=255, default='', blank=False)
    categoria = models.CharField(max_length=30, choices=Categoria.choices)
    avaliacoes = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    estoque = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    criadoEm = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
    
