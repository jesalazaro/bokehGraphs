from django.urls import path
from .import views 

urlpatterns = [
    path("starter/", views.starter, name="starter")
]
