import { Component, Input } from '@angular/core';
import { Material } from '../../utility/modules';
import { Patient } from '../../utility/types';
import { PrescriptionComponent } from '../prescription/prescription.component';
import { AppointmentComponent } from '../appointment/appointment.component';
import { ImmunizationComponent } from '../immunization/immunization.component';

@Component({
  selector: 'patient-chart',
  standalone: true,
  imports: [...Material, PrescriptionComponent, AppointmentComponent, ImmunizationComponent],
  templateUrl: './patient-chart.component.html',
  styleUrl: './patient-chart.component.scss'
})
export class PatientChartComponent {
  @Input() patientData?: Patient;


  constructor() {
    this.patientData = {
      id: 0,
      name: '',
      email: '',
      phoneNumber: '',
      doctors: [],
      address: '',
      prescriptions: [],
      immunizations: [],
      appointments: [],
    }
  }

  public getDate(time: number): Date {
    return new Date(time);
  }
}
