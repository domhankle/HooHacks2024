from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User, Doctor, Patient
import json

@csrf_exempt
def create_user(request):
    data = json.loads(request.body)
    req_username = data.get('username', '')
    req_password = data.get('password', '')
    req_role = data.get('role', '')

    if User.objects.filter(username=req_username).exists():
        return JsonResponse(
                {'error':'User already exists!'},
                status=404)

    user_instance = User(username=req_username, password=req_password, role=req_role)
    user_instance.save()

    if req_role == 'DOCTOR':
        print('ROLE IS DOCTOR')
        doctor_instance = Doctor(username=req_username)
        doctor_instance.save()

    if req_role == 'PATIENT':
        patient_instance = Patient(username=req_username)
        patient_instance.save()

    return JsonResponse(
            {'username': req_username,
            'password':req_password,
            'role':req_role,
            'id':str(user_instance.pk)},
            status=201)

