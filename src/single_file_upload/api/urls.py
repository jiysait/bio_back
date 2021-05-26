from django.urls import path
from . import views

app_name = "single_file_upload"

urlpatterns = [
    path('single-file-upload', views.single_file_upload_view,
         name="single_file_upload"),
]
