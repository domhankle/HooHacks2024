import { Component, Inject } from '@angular/core';
import { Material } from '../../utility/modules';
import { LoginService } from '../../services/login.service';
import { SingletonService } from '../../services/singleton.service';
import { Router } from '@angular/router';

@Component({
  selector: 'sign-in-page',
  standalone: true,
  imports: [...Material],
  templateUrl: './sign-in-page.component.html',
  styleUrl: './sign-in-page.component.scss'
})
export class SignInPageComponent {
  public username = '';
  public password = '';

  constructor(@Inject(LoginService) private _loginService: LoginService,
    @Inject(SingletonService) private _singletonService: SingletonService,
    @Inject(Router) private _router: Router) {

  }


  public signIn(): void {
    this._loginService.getDoctorUser(this.username, this.password).subscribe(
      response => {
        const doctor = { id: response.doctor.id, username: response.doctor.username, password: response.doctor.password, patients: response.doctor.patients };
        this._singletonService.currentDoctor.next(doctor);
        console.log("Currently Signed in User: ", this._singletonService.currentDoctor.value);
        this._router.navigate(['dashboard']);
      },
      error => {
        console.log(error);
      });
  }
}
