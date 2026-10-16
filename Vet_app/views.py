from django.shortcuts import render
from rest_framework import viewsets

from .models import Usuario, Mascota
from .serializer import UsuarioSerializer, MascotaSerializer

# Create your views here.
def landing_page(request):
    # Renderiza la página principal de la aplicación.
    return render(request, 'index.html')

def inicio(request):
    # inicio.html está vacío; reutiliza la página principal hasta que tenga contenido propio.
    return render(request, 'index.html')

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer
