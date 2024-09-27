from django.db import models

class Cliente(models.Model):
    cpf = models.CharField(max_length=11, unique=True)
    nome = models.CharField(max_length=120)
    data_nascimento = models.DateField()
    obs = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.nome
