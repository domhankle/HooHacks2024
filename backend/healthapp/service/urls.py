from django.urls import path
from . import views

urlpatterns = [
        path('user/create', views.UserEndpoints.create_user)
]
