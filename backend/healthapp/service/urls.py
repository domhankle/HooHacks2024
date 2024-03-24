from django.urls import path
from . import views

urlpatterns = [
        path('doctor', views.UserEndpoints.get_doctor)
]
