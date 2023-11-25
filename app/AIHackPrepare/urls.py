from django.contrib import admin
from django.urls import path
from Assistant import views

urlpatterns = [
    path("", views.index),
    path("upload/<int:id>", views.upload),
    path("file/download/<int:id>", views.send_file),
]
