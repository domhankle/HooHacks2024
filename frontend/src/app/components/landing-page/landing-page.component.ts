import { Component, Inject } from '@angular/core';
import { Material } from '../../utility/modules';
import { Router } from '@angular/router';


@Component({
  selector: 'landing-page',
  standalone: true,
  imports: [...Material],
  templateUrl: './landing-page.component.html',
  styleUrl: './landing-page.component.scss'
})
export class LandingPageComponent {
  
  constructor(@Inject(Router) private _router: Router)
  {}

  public goToSignIn(): void {
    this._router.navigate(['sign-in']);
  }
}
