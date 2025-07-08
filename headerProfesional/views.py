from django.shortcuts import render, redirect, get_object_or_404
from .models import Header
from .forms import HeaderForm
from .models import Habilidad
from iconos.models import Icono
from .forms import HabilidadForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from django.core.exceptions import ValidationError

@login_required
def mostrar_header(request):
    try:
        header = Header.objects.get(usuario=request.user)
    except Header.DoesNotExist:
        return redirect('crear_header')
    return render(request, 'headerProfesional/header.html', {'header': header})

@login_required
def crear_header(request):
    if Header.objects.filter(usuario=request.user).exists():
        return redirect('editar_header')

    if request.method == 'POST':
        form = HeaderForm(request.POST, request.FILES)
        if form.is_valid():
            header = form.save(commit=False)
            header.usuario = request.user
            header.save()
            form.save_m2m()  # guardar relaciones ManyToMany
            return redirect('mostrar_header')
    else:
        form = HeaderForm()

    return render(request, 'headerProfesional/form_header.html', {'form': form, 'accion': 'Crear'})

@login_required
def editar_header(request):
    header = get_object_or_404(Header, usuario=request.user)

    if request.method == 'POST':
        form = HeaderForm(request.POST, request.FILES, instance=header)
        if form.is_valid():
            form.save()
            return redirect('mostrar_header')
    else:
        form = HeaderForm(instance=header)

    return render(request, 'headerProfesional/form_header.html', {'form': form, 'accion': 'Editar'})

@login_required
def eliminar_header(request):
    header = get_object_or_404(Header, usuario=request.user)

    if request.method == 'POST':
        header.delete()
        return redirect('crear_header')

    return render(request, 'headerProfesional/eliminar_header.html', {'header': header})

@login_required
def lista_habilidades(request):
    habilidades_list = Habilidad.objects.filter(usuario=request.user).order_by('nombre')
    paginator = Paginator(habilidades_list, 6)  # 6 habilidades por página

    page_number = request.GET.get('page')
    habilidades = paginator.get_page(page_number)

    return render(request, 'habilidades/lista.html', {'habilidades': habilidades})

@login_required
def crear_habilidad(request):
    if request.method == 'POST':
        form = HabilidadForm(request.POST, user=request.user)
        if form.is_valid():
            habilidad = form.save(commit=False)
            habilidad.usuario = request.user
            try:
                habilidad.save()
                return redirect('lista_habilidades')
            except ValidationError as e:
                # Agrega los errores al formulario para que se muestren en el template
                form.add_error(None, e)  # 'None' se usa para errores generales (non_field_errors)
    else:
        form = HabilidadForm(user=request.user)

    return render(request, 'habilidades/form.html', {'form': form})

@login_required
def editar_habilidad(request, pk):
    habilidad = get_object_or_404(Habilidad, pk=pk, usuario=request.user)
    if request.method == 'POST':
        form = HabilidadForm(request.POST, instance=habilidad, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Habilidad "{habilidad.nombre}" editada correctamente.')
            return redirect('lista_habilidades')
    else:
        form = HabilidadForm(instance=habilidad, user=request.user)
    return render(request, 'habilidades/form.html', {'form': form})

@login_required
def eliminar_habilidad(request, pk):
    habilidad = get_object_or_404(Habilidad, pk=pk, usuario=request.user)
    if request.method == 'POST':
        habilidad.delete()
        return redirect('lista_habilidades')
    return render(request, 'habilidades/confirmar_eliminar.html', {'habilidad': habilidad})
