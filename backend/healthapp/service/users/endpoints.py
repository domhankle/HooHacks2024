from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ..models import User, Doctor, Patient, Appointment, Vitals, Prescription, Immunization
from django.contrib.auth import authenticate, login
import json
from django.core import serializers

def is_patient(user):
    return hasattr(user, 'patient')

def is_doctor(user):
    return hasattr(user, 'doctor')

@csrf_exempt
def get_doctor(request):
    username = request.GET.get('username')
    password = request.GET.get('password')

    try:
        doctor = Doctor.objects.get(username=username)
        if doctor.password != password:
            raise ValueError

        patient_out = []

        for patient in doctor.patients.all():
            pat_appts = []
            for appt in patient.appointments.all():
                appt_json = {
                    'date': appt.date,
                    'doctor': appt.doctor.name,
                    'complete': appt.complete,
                    'vitals':
                    {
                        'weight': appt.vitals.weight,
                        'height': appt.vitals.height
                    },
                    'notes': appt.notes,
                    'reasonForVisit': appt.reason_for_visit
                }

                pat_appts.append(appt_json)

            pat_prescriptions = []
            for pres in patient.prescriptions.all():
                pres_json = {
                    'name': pres.name,
                    'start': pres.start,
                    'end': pres.end,
                    'refill': pres.refill
                }

                pat_prescriptions.append(pres_json)

            pat_imm = []
            for imm in patient.immunizations.all():
                imm_json = {
                    "name": imm.name,
                    "upToDate": imm.up_to_date,
                    "expires": imm.expires
                }

                pat_imm.append(imm_json)

            pat_json = {
                'name': patient.name,
                'email': patient.email,
                'phoneNumber': patient.phone,
                'address': patient.address,
                'appointments': pat_appts,
                'prescriptions': pat_prescriptions,
                'immunizations': pat_imm
            }

            patient_out.append(pat_json)

        doctor_data = {
            'id': doctor.id,
            'username': doctor.username,
            'password': doctor.password,
            'patients': patient_out
        }


        return JsonResponse({
            'doctor':doctor_data
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
        'id': doctor.id,
        'name': name,
        'username': username,
        'password': password
    })

@csrf_exempt
def create_patient(request):
    data = json.loads(request.body)
    patient = Patient.objects.create(
        name = data.get('name'),
        email = data.get('email'),
        phone = data.get('phone'),
        address = data.get('address')
    )

    doctors = data.get('doctors')
    if doctors:
        for doc_id in doctors:
            try:
                doctor = Doctor.objects.get(id=doc_id)
                patient.doctors.add(doctor)
            except Exception:
                continue

    appointments = data.get('appointments')
    if appointments:
        for appt_json in appointments:
            appt = Appointment.objects.create(
                date=appt_json.get('date'),
                complete=appt_json.get('complete'),
                reason_for_visit=appt_json.get('reason'),
                notes=appt_json.get('notes')
            )
            appt.doctor.add(Doctor.objects.get(id=appt_json.get('doctor_id')))

            vitals_json = appt_json.get('vitals')
            if vitals_json:
                vitals = Vitals.objects.create(
                    weight=vitals_json.get('weight'),
                    height=vitals_json.get('height')
                )
                vitals.save()
                appt.vitals = vitals  # Assign the created Vitals object to the appointment

            appt.save()
            patient.appointments.add(appt)
    
    prescriptions = data.get('prescriptions')
    if prescriptions:
        for pres_json in prescriptions:
            pres = Prescription.objects.create(
                name = pres_json.get('name'),
                start = pres_json.get('start'),
                end = pres_json.get('end'),
                refill = pres_json.get('refill')
            )

            pres.save()

            patient.prescriptions.add(pres)
    
    immunizations = data.get('immunizations')
    if immunizations:
        for imm_json in immunizations:
            imm = Immunization.objects.create(
                name = imm_json.get('name'),
                up_to_date = imm_json.get('up_to_date'),
                expires = imm_json.get('expires')
            )

            imm.save()

            patient.immunizations.add(imm)

    patient.save()

    doc = Doctor.objects.get(id=data.get('doc_id'))
    doc.patients.add(patient)
    doc.save()

    outdoc = []
    for dr in patient.doctors.all():
        outdoc.append(dr.name)

    return JsonResponse({
        'doctorToAdd': doc.name,
        'name': patient.name,
        'username': patient.username,
        'password': patient.password,
        'email': patient.email,
        'phone': patient.phone,
        'address': patient.address,
        'doctors': outdoc,
        'appointments': appointments,
        'prescriptions': prescriptions,
        'immunizations': immunizations
    })

def fake_patients():
    return []

    

                



        
