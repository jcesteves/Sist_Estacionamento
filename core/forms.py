from django.forms import ModelForm
from .models import Pessoa, Veiculo, Movrot, Mensalista, Movmen



class Pessoaform(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'


class Veiculoform(ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__'


class Movrotform(ModelForm):
    class Meta:
        model = Movrot
        fields = '__all__'


class Mensalistaform(ModelForm):
    class Meta:
        model = Mensalista
        fields = '__all__'


class Movmenform(ModelForm):
    class Meta:
        model = Movmen
        fields = '__all__'
