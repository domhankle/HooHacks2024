import { Injectable } from '@angular/core';
import { Doctor, Patient } from '../utility/types';
import { BehaviorSubject, Subject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SingletonService {

  currentDoctor: BehaviorSubject<Doctor> = new BehaviorSubject<Doctor>(
    { id: -1, username: '', password: '', patients: [] }
  );

}
