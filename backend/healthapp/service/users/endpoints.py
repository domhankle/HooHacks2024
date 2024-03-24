from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User, Doctor, Patient
from django.contrib.auth import authenticate, login
import json

def is_patient(user):
    return hasattr(user, 'patient')

def is_doctor(user):
    return hasattr(user, 'doctor')

@csrf_exempt
def get_doctor(request):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')

    user = User.objects.get(username=username)
    if user is None:
        return JsonResponse({'error': 'Login failed'}, status=401)
    elif is_doctor(user):
        patient_list = list(user.patients.all())
        patient_out = []

        # for patient in patient_list:
        #     patient_out.append({

        #     })

        doctor = {
            'username': user.username,
            'password': user.password,
            'patients': []
        }


        return JsonResponse({
            'doctor':doctor
        })

        
