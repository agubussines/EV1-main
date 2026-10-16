from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('index/', views.landing_page, name='index'),
    path('inicio/', views.inicio, name='inicio'),
    path('api/', include('Vet_app.api_urls')),
]