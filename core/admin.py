from django.contrib import admin
from .models import (Pessoa,
                     Veiculo,
                     Parametros,
                     Movrot,
                     Mensalista,
                     Movmen,
                     )

class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'placa')


class Movrotadmin(admin.ModelAdmin):
    list_display = ('veiculo', 'checkin', 'checkout', 'valor_hora', 'total', 'horas_total', 'pago')

class Movmenadmin(admin.ModelAdmin):
    list_display = ('mensalista', 'dt_pagto', 'total')


admin.site.register(Pessoa)
admin.site.register(Veiculo, VeiculoAdmin)
admin.site.register(Parametros)
admin.site.register(Movrot, Movrotadmin)
admin.site.register(Mensalista)
admin.site.register(Movmen, Movmenadmin)
