from django.urls import path
from apps.surveys import views


urlpatterns = [
    path('all/', views.SurveysView.as_view({'get': 'all'})),
    path('<int:obj_id>/', views.SurveysView.as_view(
        {'get': 'one',
         'post': 'set_answer'}
    ))
]
