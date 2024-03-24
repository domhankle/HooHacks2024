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
  public animateOwl: boolean = false;
  public animateHeader: boolean = false;
  constructor(@Inject(Router) private _router: Router) {
  }

  public goToSignIn(): void {
    this.animateOwl = true;

    setTimeout(() => {
      this.animateOwl = false;
      this.animateHeader = true;
      setTimeout(() => {
        this.animateHeader = false;
        this._router.navigate(['sign-in']);
      }, 500)


    }, 500)

  }
}
