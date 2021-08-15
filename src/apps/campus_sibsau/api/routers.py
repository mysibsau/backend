from rest_framework.routers import DefaultRouter
from apps.campus_sibsau.api import views


router = DefaultRouter()
router.register(r'ensembles', views.EnsembleApiView)