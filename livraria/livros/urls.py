from rest_framework import routers
from .viewsets import LivroViewSet


router = routers.SimpleRouter()
router.register(r'livros', LivroViewSet)
urlpatterns = router.urls