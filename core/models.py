from django.db import models
import uuid
# Create your models here.



class Produto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=9)
    estoque = models.IntegerField('Quantidade em Estoque')
    
    def __str__(self):
        return self.nome
    
    
class Cliente(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome        = models.CharField('Nome', max_length=100)
    sobrenome   = models.CharField('Sobrenome', max_length=100)
    email       = models.EmailField('E-mail', max_length=100)
    
    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
    
    
    
    