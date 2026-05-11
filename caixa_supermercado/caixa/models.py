from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/')
    cor = models.CharField(max_length=7, default='#FFF2E5')
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
