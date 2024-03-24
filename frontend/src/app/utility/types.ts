
export interface Patient{
    id: number,
    username: string,
    password: string,
    email: string,
    phoneNumber: string,
    doctors: Doctor[],
}

export interface Doctor{
    id: number,
    username: string,
    password: string,
    patients: Patient[]
}

