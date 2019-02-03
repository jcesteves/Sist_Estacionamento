from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import (Pessoa,
                     Veiculo,
                     Movrot,
                     Mensalista,
                     Movmen,
                     )

from .forms import Pessoaform, Veiculoform, Movrotform, Mensalistaform, Movmenform

@login_required
def home(request):
    return render(request, 'core/home.html')


@login_required
def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = Pessoaform()
    data = {'pessoas': pessoas, 'form': form}
    return render(request, 'core/lista_pessoas.html', data)


@login_required
def pessoa_nova(request):
    form = Pessoaform(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoas')


@login_required
def pessoa_update(request, id):
    data = {}
    pessoa = Pessoa.objects.get(id=id)
    form = Pessoaform(request.POST or None, instance=pessoa)
    data['pessoa'] = pessoa
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_pessoas')

    else:
        return render(request, 'core/update_pessoa.html', data)


@login_required
def pessoa_delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/delete.html', {'obj': pessoa})


@login_required
def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    form = Veiculoform()
    data = {'veiculos': veiculos, 'form': form}
    return render(request, 'core/lista_veiculos.html', data)


@login_required
def veiculo_novo(request):
    form = Veiculoform(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_veiculos')


@login_required
def veiculo_update(request, id):
    data = {}
    veiculo = Veiculo.objects.get(id=id)
    form = Veiculoform(request.POST or None, instance=veiculo)
    data['veiculo'] = veiculo
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/update_veiculo.html', data)


@login_required
def veiculo_delete(request, id):
    veiculo = Veiculo.objects.get(id=id)
    if request.method == 'POST':
        veiculo.delete()
        return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/delete.html', {'obj': veiculo})


@login_required
def lista_movrotativos(request):
    mov_rotativos = Movrot.objects.all()
    form = Movrotform()
    data = {'mov_rotativos': mov_rotativos, 'form': form}
    return render(request, 'core/lista_movrot.html', data)


@login_required
def movrot_novo(request):
    form = Movrotform(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movrot')


@login_required
def movrot_update(request, id):
    data = {}
    movrot = Movrot.objects.get(id=id)
    form = Movrotform(request.POST or None, instance=movrot)
    data['movrot'] = movrot
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movrot')
    else:
        return render(request, 'core/update_movrot.html', data)


@login_required
def movrot_delete(request, id):
    movrot = Movrot.objects.get(id=id)
    if request.method == 'POST':
        movrot.delete()
        return redirect('core_lista_movrot')
    else:
        return render(request, 'core/delete.html', {'obj': movrot})


@login_required
def lista_mensalistas(request):
    mensalistas = Mensalista.objects.all()
    form = Mensalistaform()
    data = {'mensalistas': mensalistas, 'form': form}
    return render(request, 'core/lista_mensalistas.html', data)


@login_required
def mensalista_novo(request):
    form = Mensalistaform(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mensalistas')


@login_required
def mensalista_update(request, id):
    data = {}
    mensalista = Mensalista.objects.get(id=id)
    form = Mensalistaform(request.POST or None, instance=mensalista)
    data['mensalista'] = mensalista
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_mensalistas')
    else:
        return render(request, 'core/update_mensalista.html', data)


@login_required
def mensalista_delete(request, id):
    mensalista = Mensalista.objects.get(id=id)
    if request.method == 'POST':
        mensalista.delete()
        return redirect('core_lista_mensalistas')
    else:
        return render(request, 'core/delete.html', {'obj': mensalista})


@login_required
def lista_movmensalistas(request):
    mov_mensalistas = Movmen.objects.all()
    form = Movmenform()
    data = {'mov_mensalistas': mov_mensalistas, 'form': form}
    return render(request, 'core/lista_movmensalistas.html', data)


def movmen_novo(request):
    form = Movmenform(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movmensalistas')


@login_required
def movmen_update(request, id):
    data = {}
    movmen = Movmen.objects.get(id=id)
    form = Movmenform(request.POST or None, instance=movmen)
    data['movmen'] = movmen
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movmensalistas')
    else:
        return render(request, 'core/update_movmen.html', data)


@login_required
def movmen_delete(request, id):
    movmen = Movmen.objects.get(id=id)
    if request.method == 'POST':
        movmen.delete()
        return redirect('core_lista_movmensalistas')
    else:
        return render(request, 'core/delete.html', {'obj': movmen})
