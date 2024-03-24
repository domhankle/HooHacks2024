import { Injectable } from '@angular/core';
import { Doctor, Patient } from '../utility/types';
import { BehaviorSubject, Subject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SingletonService {

  currentUser: BehaviorSubject<Doctor | Patient> = new BehaviorSubject<Doctor | Patient>(
    { id: -1, username: '', password: '', patients: [] }
  );

}
