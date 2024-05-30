from django.db import models

# Create your models here.

class Categoria(models.TextChoices):
    CATEGORIAS = {
    "Celulares": {
        "smartphone": "Smartphones",
        "tablet": "Tablets",
        "acessorio": "Acessorios"
    },
    "Computadores": {
        "notebook": "VHS Tape",
        "dvd": "DVD",
    },
    "unknown": "Unknown",
}

class Produto(models.Model):
    nome = models.CharField(max_length=255, default='', blank=False)
    descricao = models.TextField(max_length=1000, default='', blank=False)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    marca = models.CharField(max_length=255, default='', blank=False)

