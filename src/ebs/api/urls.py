from django.urls import path
from . import views

app_name = "ebs"

urlpatterns = [
    path('analysis/open', views.open_analysis_view,
         name="open_analysis"),
    path('sequence/add', views.add_sequence_view,
         name="add_sequence"),
]