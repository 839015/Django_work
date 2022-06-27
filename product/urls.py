from product.views import ProductOperations
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('api', ProductOperations)
urlpatterns = router.urls
