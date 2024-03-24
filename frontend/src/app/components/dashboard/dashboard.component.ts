import { Component, Inject } from '@angular/core';
import { Material } from '../../utility/modules';
import { Doctor, Patient } from '../../utility/types';
import { SingletonService } from '../../services/singleton.service';
import { paginateData } from '../../utility/functions';
import { PageEvent } from '@angular/material/paginator';

@Component({
  selector: 'dashboard',
  standalone: true,
  imports: [...Material],
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.scss'
})
export class DashboardComponent {

  public doctor: Doctor;
  public displayedColumns: string[] = ['name', 'email', 'phone number', 'address']

  public paginatedData: Patient[] = [];

  public patientShown?: Patient
  public viewingPatient = false;



  public constructor(@Inject(SingletonService) private _singletonService: SingletonService) {
    this.doctor = this._singletonService.currentDoctor.value;

    // this.doctor = {
    //   id: 1,
    //   username: 'joe',
    //   password: 'lol',
    //   patients: [
    //     {
    //       name: 'Patient 1',
    //       email: 'joe@gmail.com',
    //       phoneNumber: '757-276-9417',
    //       address: '1800 Huckleberry Ln.'
    //     },
    //     {
    //       name: 'Patient 1',
    //       email: 'joe@gmail.com',
    //       phoneNumber: '757-276-9417',
    //       address: '1800 Huckleberry Ln.'
    //     },
    //     {
    //       name: 'Patient 1',
    //       email: 'joe@gmail.com',
    //       phoneNumber: '757-276-9417',
    //       address: '1800 Huckleberry Ln.'
    //     },
    //     {
    //       name: 'Patient 1',
    //       email: 'joe@gmail.com',
    //       phoneNumber: '757-276-9417',
    //       address: '1800 Huckleberry Ln.'
    //     },
    //     {
    //       name: 'Patient 1',
    //       email: 'joe@gmail.com',
    //       phoneNumber: '757-276-9417',
    //       address: '1800 Huckleberry Ln.'
    //     },
    //   ] as unknown as Patient[]
    // }

    this.paginatedData = paginateData(this.doctor.patients, 0, 4);
  }

  public handlePaging(event: PageEvent): void {
    console.log(event);
    this.paginatedData = paginateData(this.doctor.patients, event.pageIndex, event.pageSize);
  }
}
