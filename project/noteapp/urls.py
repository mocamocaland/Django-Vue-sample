from rest_framework.routers import DefaultRouter
from .views import PageViewSet

router = DefaultRouter()
router.register(r'pages', PageViewSet, base_name='page')
urlpatterns = router.urls
