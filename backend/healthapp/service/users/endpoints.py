from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ..models import User, Doctor, Patient
from django.contrib.auth import authenticate, login
import json

def is_patient(user):
    return hasattr(user, 'patient')

def is_doctor(user):
    return hasattr(user, 'doctor')

@csrf_exempt
def get_doctor(request):
    username = request.GET.get('username')
    password = request.GET.get('password')

    try:
        user = User.objects.get(username=username)
        
        if user.password != password:
            raise ValueError

        if is_doctor(user):
            patient_list = list(user.patients.all())
            patient_out = []

            for patient in patient_list:
                patient_out.append({

                })

            doctor = {
                'username': user.username,
                'password': user.password,
                'patients': []
            }


            return JsonResponse({
                'doctor':doctor
            })
    except User.DoesNotExist:
        return JsonResponse({'error': 'User does not exist'}, status=404)
    except ValueError:
        return JsonResponse({'error': 'Incorrect Password'}, status=401)

@csrf_exempt
def create_doctor(request):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    name = data.get('name')

    doctor = Doctor.objects.create(username=username, password=password, name=name)

    doctor.save()

    return JsonResponse({
        'name': name,
        'username': username,
        'password': password
    })

        
