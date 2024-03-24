import { Routes } from '@angular/router';
import { LandingPageComponent } from './components/landing-page/landing-page.component';
import { SignInPageComponent } from './components/sign-in-page/sign-in-page.component';
import { DashboardComponent } from './components/dashboard/dashboard.component';

export const routes: Routes = [
    { path: '', component: LandingPageComponent },
    { path: 'sign-in', component: SignInPageComponent },
    { path: 'dashboard', component: DashboardComponent }];
