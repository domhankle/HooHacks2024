import { Component, Input } from '@angular/core';
import { Immunization } from '../../utility/types';
import { Material } from '../../utility/modules';
import { DatePipe } from '@angular/common';

@Component({
  selector: 'immunization',
  standalone: true,
  imports: [...Material, DatePipe],
  templateUrl: './immunization.component.html',
  styleUrl: './immunization.component.scss'
})
export class ImmunizationComponent {
  @Input() public immunizationData?: Immunization;

  public getExpirationDate(): Date {
    return new Date(this.immunizationData!.expires);
  }
}
