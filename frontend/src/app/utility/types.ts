import internal from "stream"

export interface Patient {
    id: number,
    username: string,
    password: string,
    name: string,
    email: string,
    phoneNumber: string,
    doctors: Doctor[],
    address: string,
    prescriptions: Prescription[],
    immunizations: Immunization[],
    appointments: Appointment[],
}

export interface Appointment {
    date: number,
    doctor: Doctor,
    complete: boolean,
    vitals: Vitals,
    notes: string,
    reasonForVisit: string
}


export interface Vitals {
    weight: number,
    height: number
}

export interface Immunization {
    name: string,
    upToDate: boolean,
    expires: number
}

export interface Prescription {
    name: string,
    start: number,
    end: number,
    refill: boolean
}

export interface Doctor {
    id: number,
    username: string,
    password: string,
    patients: Patient[]
}

