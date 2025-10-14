import { Routes } from '@angular/router';
import { authGuard, permissionGuard } from '@abp/ng.core';
import { BookComponent } from './book/book';

export const APP_ROUTES: Routes = [
  {
    path: 'books',
    canActivate: [authGuard, permissionGuard],
    loadComponent: () => import('./book/book').then(m => m.BookComponent),
  },
  {
    path: 'authors',
    canActivate: [authGuard, permissionGuard],
    loadComponent: () => import('./author/author').then(m => m.AuthorComponent),
  },
  {
    path: 'books/:id',
    canActivate: [authGuard, permissionGuard],
    loadComponent: () => import('./book/book').then(m => m.BookComponent),
  },
  {
    path: '',
    pathMatch: 'full',
    loadComponent: () => import('./home/home.component').then(c => c.HomeComponent),
  },
  {
    path: 'account',
    loadChildren: () => import('@abp/ng.account').then(c => c.createRoutes()),
  },
  {
    path: 'identity',
    loadChildren: () => import('@abp/ng.identity').then(c => c.createRoutes()),
  },
  {
    path: 'tenant-management',
    loadChildren: () => import('@abp/ng.tenant-management').then(c => c.createRoutes()),
  },
  {
    path: 'setting-management',
    loadChildren: () => import('@abp/ng.setting-management').then(c => c.createRoutes()),
  },
];
