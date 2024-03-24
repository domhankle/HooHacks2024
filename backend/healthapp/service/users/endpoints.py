from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ..models import User, Doctor, Patient
from django.contrib.auth import authenticate, login
import json

def is_patient(user):
    return hasattr(user, 'patient')

def is_doctor(user):
    return hasattr(user, 'doctor')

def fake_patients():
    return [{
        'name': 'Domenic Hankle',
        'email': 'dhank003@gmail.com',
        'phoneNumber': '757-394-6969',
        'address': "4200 Huckleberry Trail, Virginia Beach, VA",
        'appointments':
        [{
            'date': 3020302,
            'doctor': 'Dr. T-Pain',
            'complete': True,
            'vitals':
            {
                'weight': 8000,
                'height': 4
            },
            'notes': 'Bro took a shit on the hospital bed.',
            'reason_for_visit': 'Excessive peeing'
        },
        {
            'date': 289342,
            'doctor': 'Dr. Penis',
            'complete': False,
            'vitals':{},
            'notes': 'wtfff.',
            'reason_for_visit': 'Drank Norfolk water.'
        }],
        'prescriptions': 
        [{
            'name': 'Comethazine',
            'start': 0,
            'end': 1000000,
            'refill': True
        },
        {
            'name': 'Soggy Crispers',
            'start': 33,
            'end': 489489,
            'refill': False
        }],
        'immunizations': 
        [{
            "name": "Rabies",
            "up_to_date": False,
            "expires": 567
        },
        {
            "name": "running out of ideas",
            "up_to_date": True,
            "expires": 78483789743
        }]

    },
    {
        'name': 'Anthony Vecchio',
        'email': 'dapie125@gmail.com',
        'phoneNumber': '757-339-7969',
        'address': '4227 Hunt Club Circle, Fairfax, VA',
        'appointments':
        [{
            'date': 3020302,
            'doctor': 'Dr. T-Pain',
            'complete': True,
            'vitals':
            {
                'weight': 0,
                'height': 59
            },
            'notes': 'fiended over black women.',
            'reason_for_visit': 'homosexual tendencies'
        },
        {
            'date': 289342,
            'doctor': 'Dr. Penis',
            'complete': False,
            'vitals':{},
            'notes': 'wtfff.',
            'reason_for_visit': 'eat without youtube.'
        }],
        'prescriptions': 
        [{
            'name': 'PeanutButterPretzels',
            'start': 0,
            'end': 1000000,
            'refill': True
        },
        {
            'name': 'Black Pussy',
            'start': 33,
            'end': 489489,
            'refill': False
        }],
        'immunizations': 
        [{
            "name": "idk",
            "up_to_date": False,
            "expires": 567
        },
        {
            "name": "bruhhhhh",
            "up_to_date": True,
            "expires": 78483789743
        }]
    },
    {
        'name': 'Grady Insley',
        'email': 'dagradster@gmail.com',
        'phoneNumber': '757-696-9988',
        'address': 'MIDQUOSON HELL NAW',
        'appointments':
        [{
            'date': 3020302,
            'doctor': 'Dr. Penja Mon',
            'complete': True,
            'vitals':
            {
                'weight': 200000,
                'height': 200
            },
            'notes': 'Worked on dnd campaign all appt.',
            'reason_for_visit': 'homosexual tendencies'
        },
        {
            'date': 289342,
            'doctor': 'Dr. Penis',
            'complete': False,
            'vitals':{},
            'notes': 'wtfff.',
            'reason_for_visit': 'eat without youtube.'
        }],
        'prescriptions': 
        [{
            'name': 'Lean',
            'start': 0,
            'end': 1000000,
            'refill': True
        },
        {
            'name': 'Toke',
            'start': 33,
            'end': 489489,
            'refill': False
        }],
        'immunizations': 
        [{
            "name": "HIV/AIDS",
            "up_to_date": False,
            "expires": 567
        },
        {
            "name": "Flu",
            "up_to_date": True,
            "expires": 78483789743
        }]
    },
    {
        'name': 'Ross Insley',
        'email': 'ilovedestiny@gmail.com',
        'phoneNumber': '757-idkmf',
        'address': 'something Sandy Bay Dr, Virginia Beach, VA',
        'appointments':
        [{
            'date': 3020302,
            'doctor': 'Dr. Sukuna',
            'complete': True,
            'vitals':
            {
                'weight': 200000,
                'height': 200
            },
            'notes': 'what do i even write here.',
            'reason_for_visit': 'also homosexual tendencies'
        },
        {
            'date': 289342,
            'doctor': 'Dr. Penis',
            'complete': False,
            'vitals':{},
            'notes': 'kms.',
            'reason_for_visit': 'valorant player.'
        }],
        'prescriptions': 
        [{
            'name': 'vitaminwater',
            'start': 0,
            'end': 1000000,
            'refill': True
        },
        {
            'name': 'everclear',
            'start': 33,
            'end': 489489,
            'refill': False
        }],
        'immunizations': 
        [{
            "name": "random shit",
            "up_to_date": False,
            "expires": 567
        },
        {
            "name": "Flu",
            "up_to_date": True,
            "expires": 78483789743
        }]
    }]


@csrf_exempt
def get_doctor(request):
    username = request.GET.get('username')
    password = request.GET.get('password')

    try:
        user = Doctor.objects.get(username=username)
        
        if user.password != password:
            raise ValueError

        if user.patients.exists():
            patient_list = list(user.patients.all())
            patient_out = []

            for patient in patient_list:
                patient_out.append({

                })

        doctor = {
            'id': user.id,
            'username': user.username,
            'password': user.password,
            'patients': fake_patients()
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

        
