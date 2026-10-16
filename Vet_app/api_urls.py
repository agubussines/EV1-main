from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('usuarios', views.UsuarioViewSet)
router.register('mascotas', views.MascotaViewSet)

urlpatterns = router.urls