from django.shortcuts import render, get_object_or_404, redirect
from .models import Certificacion
from headerProfesional.models import Header
from headerProfesional.models import Habilidad
from objetivo.models import ObjetivoProfesional
from proyectos.models import Proyecto
from .forms import CertificacionForm
from django.contrib.auth.decorators import login_required   
from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa
from io import BytesIO
from django.core.paginator import Paginator


@login_required
def certificacion_list(request):
    certificaciones_list = Certificacion.objects.filter(usuario=request.user)
    paginator = Paginator(certificaciones_list, 4)  

    page_number = request.GET.get('page')
    certificaciones = paginator.get_page(page_number)

    return render(request, 'certificaciones/certificacion_list.html', {'certificaciones': certificaciones})

@login_required
def certificacion_create(request):
    if request.method == 'POST':
        form = CertificacionForm(request.POST, request.FILES)
        if form.is_valid():
            certificacion = form.save(commit=False)
            certificacion.usuario = request.user
            certificacion.save()
            return redirect('certificacion_list')
    else:
        form = CertificacionForm()
    return render(request, 'certificaciones/certificacion_form.html', {'form': form})

@login_required
def certificacion_update(request, pk):
    certificacion = get_object_or_404(Certificacion, pk=pk, usuario=request.user)
    if request.method == 'POST':
        form = CertificacionForm(request.POST, request.FILES, instance=certificacion)
        if form.is_valid():
            form.save()
            return redirect('certificacion_list')
    else:
        form = CertificacionForm(instance=certificacion)
    return render(request, 'certificaciones/certificacion_form.html', {'form': form})

@login_required
def certificacion_delete(request, pk):
    certificacion = get_object_or_404(Certificacion, pk=pk, usuario=request.user)
    if request.method == 'POST':
        certificacion.delete()
        return redirect('certificacion_list')
    return render(request, 'certificaciones/certificacion_confirm_delete.html', {'certificacion': certificacion})



def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def generar_pdf(request):
    header = Header.objects.filter(usuario=request.user).first()
    habilidades_lista = Habilidad.objects.filter(usuario=request.user)
    objetivos = ObjetivoProfesional.objects.filter(usuario=request.user)   
    proyectos = Proyecto.objects.filter(usuario=request.user)
    certificaciones = Certificacion.objects.filter(usuario=request.user)
    
    context = {
        'header': header,
        'habilidades_lista': habilidades_lista,
        'objetivos': objetivos,
        'proyectos': proyectos,
        'certificaciones': certificaciones,
    }

    return render_to_pdf('certificaciones/plantilla_pdf.html', context)


