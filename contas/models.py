from django.db import models

# Create your models here.
class Categoria (models.Model):
    nome = models.CharField(max_length=100)
    dtcria = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
    
class Transacao (models.Model):
    data = models.DateTimeField()
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    obs = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'tranca'

    def __str__(self):
        return self.descricao
    