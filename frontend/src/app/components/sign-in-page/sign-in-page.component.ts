import { Component } from '@angular/core';
import { Material } from '../../utility/modules';

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


  public signIn(): void {
    console.log("Username: ", this.username);
    console.log("Password: ", this.password);
  }
}
