import { Component, Input } from '@angular/core';
import { Material } from '../../utility/modules';
import { DatePipe } from '@angular/common';

@Component({
  selector: 'prescription',
  standalone: true,
  imports: [...Material, DatePipe],
  templateUrl: './prescription.component.html',
  styleUrl: './prescription.component.scss'
})
export class PrescriptionComponent {
  @Input() name?: string;
  @Input() start?: Date;
  @Input() end?: Date;
  @Input() refill?: boolean
}
