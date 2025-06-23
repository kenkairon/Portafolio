from django.shortcuts import render
from headerProfesional.models import Header
from objetivo.models import ObjetivoProfesional
from proyectos.models import Proyecto
from certificaciones.models import Certificacion
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    usuario = request.user

    header = Header.objects.filter(usuario=usuario).first()  # si tenés uno por usuario
    objetivos = ObjetivoProfesional.objects.filter(usuario=request.user).order_by('orden')
    proyectos = Proyecto.objects.filter(usuario=usuario, estado='completado')
    certificaciones = Certificacion.objects.filter(usuario=usuario)

    context = {
        'header': header,
        'objetivos': objetivos,
        'proyectos': proyectos,
        'certificaciones': certificaciones,
    }
    return render(request, 'home/home.html', context)
