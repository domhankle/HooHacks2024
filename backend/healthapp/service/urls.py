from django.urls import path
from .users import endpoints as UserEndpoints

urlpatterns = [
        path('doctor', UserEndpoints.get_doctor)
]
