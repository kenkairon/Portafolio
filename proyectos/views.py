from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Proyecto
from .forms import ProyectoForm
@login_required
def lista_proyectos(request):
    proyectos_lista = Proyecto.objects.filter(usuario=request.user).order_by('-fecha_inicio')
    
    paginator = Paginator(proyectos_lista, 5)  # 5 proyectos por página
    page_number = request.GET.get('page')
    proyectos = paginator.get_page(page_number)

    return render(request, 'proyectos/lista_proyectos.html', {'proyectos': proyectos})

@login_required
def detalle_proyecto(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk, usuario=request.user)
    return render(request, 'proyectos/detalle_proyecto.html', {'proyecto': proyecto})

@login_required
def nuevo_proyecto(request):
    if request.method == "POST":
        form = ProyectoForm(request.POST)
        if form.is_valid():
            proyecto = form.save(commit=False)
            proyecto.usuario = request.user
            proyecto.save()
            return redirect('lista_proyectos')
    else:
        form = ProyectoForm()
    return render(request, 'proyectos/editar_proyecto.html', {'form': form})

@login_required
def editar_proyecto(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk, usuario=request.user)
    if request.method == "POST":
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            proyecto = form.save(commit=False)
            proyecto.usuario = request.user
            proyecto.save()
            return redirect('lista_proyectos')
    else:
        form = ProyectoForm(instance=proyecto)
    return render(request, 'proyectos/editar_proyecto.html', {'form': form})

@login_required
def eliminar_proyecto(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk, usuario=request.user)
    proyecto.delete()
    return redirect('lista_proyectos')
