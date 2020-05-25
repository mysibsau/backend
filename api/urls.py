from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import api.views as views

urlpatterns = [
     path('groups/', views.GroupView.as_view({'get': 'all'})),
     path('places/', views.PlaceView.as_view({'get': 'all'})),
     path('professors/', views.ProfessorView.as_view({'get': 'all'})),

     path('<who>/hash/', views.HashView.as_view({'get': 'hash'})),

     path('timetable/<who>/<int:id>/<int:week>',
          views.TimetableView.as_view({'get': 'timetable'})),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
