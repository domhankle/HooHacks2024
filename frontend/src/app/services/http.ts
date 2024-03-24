import { HttpHeaders } from "@angular/common/http";
import { Doctor } from "../utility/types";

export const serverUrl = 'http://localhost:8000/service'

export const headers: HttpHeaders = new HttpHeaders({
    'Content-Type':'application/json'
  });

export interface Doctor_GET_response{
    doctor: Doctor
}


