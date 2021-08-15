from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register('faq', views.FAQViewSet)
router.register('themes', views.ThemeModelView)

urlpatterns = router.urls
