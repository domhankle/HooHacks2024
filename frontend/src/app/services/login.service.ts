import { Inject, Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, Subject } from 'rxjs';
import { serverUrl, headers, Doctor_GET_response } from './http';
import { Doctor } from '../utility/types';

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  constructor(@Inject(HttpClient) private _http: HttpClient) { }

  public getDoctorUser(username: string, password: string): Observable<Doctor_GET_response>{
    return this._http.get<Doctor_GET_response>(`${serverUrl}/doctor?username=${username}&password=${password}`, {headers: headers});
  }

}
