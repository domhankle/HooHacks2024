import { Component, Input } from '@angular/core';
import { Appointment } from '../../utility/types';
import { app } from '../../../../server';
import { Material } from '../../utility/modules';
import { DatePipe } from '@angular/common';

@Component({
  selector: 'appointment',
  standalone: true,
  imports: [...Material, DatePipe],
  templateUrl: './appointment.component.html',
  styleUrl: './appointment.component.scss'
})
export class AppointmentComponent {
  @Input() public appointmentInfo?: Appointment;

  public getAppointmentDate(): Date {
    return new Date(this.appointmentInfo!.date);
  }
}
