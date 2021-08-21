from django.db import models

# Create your models here.

class Receita(models.Model):
    nome_receita = models.CharField(max_length=255)
    tempo_preparo = models.TextField()
    rendimento = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    modo_preparo = models.TextField()
    ingredientes = models.TextField()
    data_receita = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome_receita

