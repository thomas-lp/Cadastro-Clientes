from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .forms import ClienteForm

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'listar.html', {'clientes': clientes})

def criar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm()
    return render(request, 'form.html', {'form': form})

def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'form.html', {'form': form})

def excluir_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('listar_clientes')
    return render(request, 'confirm_delete.html', {'cliente': cliente})

def buscar_cliente(request):
    query = request.GET.get('q')
    clientes = Cliente.objects.filter(nome__icontains=query) if query else Cliente.objects.all()
    return render(request, 'busca.html', {'clientes': clientes})
