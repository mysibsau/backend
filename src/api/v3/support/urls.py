from rest_framework.routers import SimpleRouter

from api.v3.support import views

router = SimpleRouter()
router.register('faq', views.FAQModelViewSet)
router.register('themes', views.ThemeModelViewSet)

urlpatterns = router.urls
