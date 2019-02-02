from django.db import models
from math import ceil

# Tabela Para definição dos valores para cálculo das horas e dias do estacionamento
class Parametros(models.Model):
    valor_hora = models.DecimalField(max_digits=5, decimal_places=2)
    valor_mes = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        verbose_name_plural = 'Parametros'

    def __str__(self):
        return 'Parâmetros Gerais'


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Veiculo(models.Model):
    marca = models.CharField(max_length=100)
    placa = models.CharField(max_length=7)
    propietario = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    cor = models.CharField(max_length=15)
    observacoes = models.TextField()

    def __str__(self):
        return self.marca + ' - ' + self.placa


class Movrot(models.Model):
    checkin = models.DateTimeField(auto_now=False)
    checkout = models.DateTimeField(auto_now=False, null=True, blank=True)
    valor_hora = models.DecimalField(max_digits=5, decimal_places=2)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    pago = models.BooleanField(default=False)


    def horas_total(self):
        return ceil((self.checkout - self.checkin).total_seconds() / 3600)

    def total(self):
        if self.horas_total() <= 1:
            return self.valor_hora
        else:
            return self.valor_hora * self.horas_total()

    def __str__(self):
        return str(self.veiculo)




class Mensalista(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    inicio = models.DateField()
    valor_mes = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return str(self.veiculo) + ' - ' + str(self.inicio)


class Movmen(models.Model):
    mensalista = models.ForeignKey(Mensalista, on_delete=models.CASCADE)
    dt_pagto = models.DateField()
    total = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return str(self.mensalista) + ' - ' + str(self.total)

