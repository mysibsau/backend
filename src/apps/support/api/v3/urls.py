from rest_framework.routers import SimpleRouter

from apps.support.api.v3 import views

router = SimpleRouter()
router.register('faq', views.FAQModelViewSet)
router.register('themes', views.ThemeModelViewSet)

urlpatterns = router.urls
