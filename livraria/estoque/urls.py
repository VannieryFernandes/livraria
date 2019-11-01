from rest_framework import routers
from .viewsets import EstoqueViewSet

router = routers.SimpleRouter()
router.register(r'estoques', EstoqueViewSet)
urlpatterns = router.urls