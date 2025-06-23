from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Icono
from .forms import IconoForm
from django.shortcuts import redirect
from django.contrib import messages


@login_required
def listar_iconos(request):
    iconos_usuario = Icono.objects.filter(usuario=request.user)
    paginator = Paginator(iconos_usuario, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'iconos/listar.html', {'page_obj': page_obj})


@login_required
def crear_icono(request):
    if request.method == 'POST':
        form = IconoForm(request.POST)
        if form.is_valid():
            icono = form.save(commit=False)
            icono.usuario = request.user  
            icono.save()
            messages.success(request, f'Ícono "{icono.nombre}" creado correctamente.')
            return redirect('listar_iconos')
    else:
        form = IconoForm()
    return render(request, 'iconos/formulario.html', {'form': form})


@login_required
def editar_icono(request, pk):
    icono = get_object_or_404(Icono, pk=pk)
    if request.method == 'POST':
        form = IconoForm(request.POST, instance=icono)
        if form.is_valid():
            form.save()
            messages.success(request, f'Ícono "{icono.nombre}" actualizado correctamente.')
            return redirect('listar_iconos')
    else:
        form = IconoForm(instance=icono)
    return render(request, 'iconos/formulario.html', {'form': form})


@login_required
def eliminar_icono(request, pk):
    icono = get_object_or_404(Icono, pk=pk)
    if request.method == 'POST':
        icono.delete()
        messages.success(request, f'Ícono "{icono.nombre}" eliminado correctamente.')
        return redirect('listar_iconos')
    return render(request, 'iconos/confirmar_eliminar.html', {'icono': icono})
