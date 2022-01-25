from rest_framework import routers
from api.v3.timetable import views


router = routers.SimpleRouter()

router.register('group', views.GroupViewSet, basename='timetable_group')
router.register('teacher', views.TeacherViewSet, basename='timetable_teacher')
router.register('place', views.PlaceViewSet, basename='timetable_teacher')

urlpatterns = router.urls
