from django.urls import path
from . import views

urlpatterns = [
    path("upload/", views.upload_file, name="file_txt"),
    path("upload/list/", views.list_stores),
]
