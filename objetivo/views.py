from django.shortcuts import render, redirect, get_object_or_404
from .models import ObjetivoProfesional
from .forms import ObjetivoForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

@login_required
def objetivo_list(request):
    lista_objetivos = ObjetivoProfesional.objects.filter(usuario=request.user)
    paginator = Paginator(lista_objetivos, 6) 

    page_number = request.GET.get('page')
    objetivos = paginator.get_page(page_number)

    return render(request, 'objetivo/list.html', {'objetivos': objetivos})
# objetivo/views.py
@login_required
def objetivo_create(request):
    if request.method == 'POST':
        form = ObjetivoForm(request.POST, user=request.user)
        if form.is_valid():
            objetivo = form.save(commit=False)
            objetivo.usuario = request.user
            objetivo.save()
            return redirect('objetivo_list')
    else:
        form = ObjetivoForm(user=request.user)
    return render(request, 'objetivo/form.html', {'form': form})

@login_required
def objetivo_update(request, pk):
    objetivo = get_object_or_404(ObjetivoProfesional, pk=pk, usuario=request.user)

    if request.method == 'POST':
        form = ObjetivoForm(request.POST, instance=objetivo, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('objetivo_list')
    else:
        form = ObjetivoForm(instance=objetivo, user=request.user)

    return render(request, 'objetivo/form.html', {'form': form})


@login_required
def objetivo_delete(request, pk):
    objetivo = get_object_or_404(ObjetivoProfesional, pk=pk, usuario=request.user)
    if request.method == 'POST':
        objetivo.delete()
        return redirect('objetivo_list')
    return render(request, 'objetivo/confirm_delete.html', {'objetivo': objetivo})
