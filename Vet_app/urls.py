from django.urls import path,include
from rest_framework import routers
from Vet_app import views

enrutador = routers.DefaultRouter()
enrutador.register(r'usuarios', views.UsuarioViewSet)
enrutador.register(r'mascotas', views.MascotaViewSet)

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('api/', include(enrutador.urls)),
]