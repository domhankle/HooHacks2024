export enum Role{
    PATIENT = 'PATIENT',
    DOCTOR = 'DOCTOR',
    ADMIN = 'ADMIN'
}

export interface User{
    id: number,
    role: string,
    username: string,
    password: string
}