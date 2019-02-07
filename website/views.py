from django.shortcuts import render
from .models import Contato

def home(request):
    return render(request, 'website/index.html')


def contato(request):
    mensagem = ''
    if request.method == 'POST':
        try:
            contato = {}
            contato['email'] = request.POST.get('email')
            contato['nome'] = request.POST.get('nome')
            contato['sobrenome'] = request.POST.get('sobrenome')
            contato['endereco'] = request.POST.get('endereco')
            contato['mensagem'] = request.POST.get('mensagem')
            contato['check'] = True if request.POST.get('check') == 'on' else False

            Contato.objects.create(**contato)
        except Exception as e:
            mensagem = str(e)

        else:
            mensagem = 'Contato efetuado com sucesso'

    return render(request, 'website/contato.html', {'mensagem': mensagem})


def servicos(request):
    return render(request, 'website/servicos.html')


def sobre(request):
    return render(request, 'website/sobre.html')


def planos(request):
    return render(request, 'website/planos.html')