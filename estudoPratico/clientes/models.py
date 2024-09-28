from django.db import models

class Cliente(models.Model):
    cpf = models.CharField(max_length=11, unique=True)
    nome = models.CharField(max_length=120)
    data_nascimento = models.DateField()
    obs = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.nome

class Contrato(models.Model):
    #related_name = 'contratos' -> serve para definir o nome do relacionamento inverso, cliente.contratos.all(), vai mostrat todos os contratos do cliente
    cliente = models.ForeignKey(Cliente, related_name='contratos', on_delete=models.CASCADE, null=True, blank=True)
    id_contrato = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    parcelas = models.IntegerField()
    texa = models.DecimalField(max_digits=5, decimal_places=2)
    parcelas_pagas = models.IntegerField()
    
    def __str__(self):
        return self.id_contrato
    
class Endereco(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    cep = models.CharField(max_length=9)
    rua = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=255)
    estado = models.CharField(max_length=2)
    pais = models.CharField(100)
    
    def __str__(self):
        return f"{self.rua}, {self.numero}"
    
class Telefone(models.Model):
    cliente = models.ForeignKey(Cliente, related_name='telefones', on_delete=models.CASCADE, null=True, blank=True)
    ddd = models.CharField(max_length=2)
    tel = models.CharField(max_length=9)
    
    def __str__(self):
        return f"({self.ddd}), {self.tel}"