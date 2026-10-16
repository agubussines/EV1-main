from django.shortcuts import render
<<<<<<< HEAD
from rest_framework import viewsets

from .models import Usuario, Mascota
from .serializer import UsuarioSerializer, MascotaSerializer
=======
>>>>>>> 96dd9e8b874e2b731393b3b765924d45f58a6fd2

# Create your views here.
def landing_page(request):
    # Esto le dice a Django que renderice el archivo hindex.html
<<<<<<< HEAD
    return render(request, 'index.html')

def inicio(request):
    return render(request, 'inicio.html')

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer





=======
    return render(request, 'index.html')
>>>>>>> 96dd9e8b874e2b731393b3b765924d45f58a6fd2
