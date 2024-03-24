import { Inject, Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { serverUrl } from './http';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor(@Inject(HttpClient) private _http: HttpClient) { }


  public getUser(username: string): Observable<User>{
    return this._http.get<User>(serverUrl, {})
  }
  {

  }
}
