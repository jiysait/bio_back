from django.urls import path
from . import views

app_name = "multiple_files_upload"

urlpatterns = [
    path('multiple-files-upload', views.multiple_files_upload_view,
         name="multiple_files_upload"),
]
