import { Component, Inject, ViewChild, input } from '@angular/core';
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

  public nonPaginatedData: Patient[] = [];
  public paginatedData: Patient[] = [];

  public patientShown?: Patient
  public viewingPatient = false;

  public searchBarValue: string = '';

  public pageIndex = 0;
  public pageSize = 4;


  public constructor(@Inject(SingletonService) private _singletonService: SingletonService) {
    this.doctor = this._singletonService.currentDoctor.value;


    this.doctor = {
      id: 1,
      username: 'joe',
      password: 'lol',
      patients: [
        {
          name: 'Joe',
          email: 'joe@gmail.com',
          phoneNumber: '757-276-9417',
          address: '1800 Huckleberry Ln.'
        },
        {
          name: 'Carl',
          email: 'joe@gmail.com',
          phoneNumber: '757-276-9417',
          address: '1800 Huckleberry Ln.'
        },
        {
          name: 'Kathy',
          email: 'joe@gmail.com',
          phoneNumber: '757-276-9417',
          address: '1800 Huckleberry Ln.'
        },
        {
          name: 'Kate',
          email: 'joe@gmail.com',
          phoneNumber: '757-276-9417',
          address: '1800 Huckleberry Ln.'
        },
        {
          name: 'Paris',
          email: 'joe@gmail.com',
          phoneNumber: '757-276-9417',
          address: '1800 Huckleberry Ln.'
        },
      ] as unknown as Patient[]
    }

    this.nonPaginatedData = [...this.doctor.patients];

    this.paginatedData = paginateData(this.nonPaginatedData, this.pageIndex, this.pageSize);
    console.log(this.paginatedData);
  }



  public handlePaging(event: PageEvent): void {
    console.log(event);
    this.pageIndex = event.pageIndex;
    this.pageSize = event.pageSize;
    this.paginatedData = paginateData(this.nonPaginatedData, this.pageIndex, this.pageSize);
  }

  public onInputChange(): void {
    if (this.searchBarValue.length > 0) {
      console.log("Value is greater than 0")
      this.nonPaginatedData = this.nonPaginatedData.filter(patient => {
        return patient.name.includes(this.searchBarValue);
      })
    }
    else {
      this.nonPaginatedData = [...this.doctor.patients];
    }

    this.paginatedData = paginateData(this.nonPaginatedData, this.pageIndex, this.pageSize);
  }
}
