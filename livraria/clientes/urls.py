from rest_framework import routers
from .viewsets import ClienteViewSet

router = routers.SimpleRouter()
router.register(r'clientes', ClienteViewSet)
urlpatterns = router.urls