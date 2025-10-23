import { Routes } from '@angular/router';
import { authGuard, permissionGuard } from '@abp/ng.core';

export const APP_ROUTES: Routes = [
  {
    path: 'books',
    canActivate: [authGuard, permissionGuard],
    loadComponent: () => import('./book/book').then(c => c.BookComponent),
  },
  {
    path: 'authors',
    canActivate: [authGuard, permissionGuard],
    loadComponent: () => import('./author/author').then(c => c.AuthorComponent),
  },
  {
    path: 'books/:id',
    canActivate: [authGuard, permissionGuard],
    loadComponent: () => import('./book/book').then(c => c.BookComponent),
  },
  {
    path: '',
    pathMatch: 'full',
    loadComponent: () => import('./home/home.component').then(c => c.HomeComponent),
  },
  {
    path: 'account',
    loadChildren: () => import('@abp/ng.account').then(c => c.AccountModule),
  },
  {
    path: 'identity',
    loadChildren: () => import('@abp/ng.identity').then(c => c.IdentityModule),
  },
  {
    path: 'tenant-management',
    loadChildren: () => import('@abp/ng.tenant-management').then(c => c.TenantManagementModule),
  },
  {
    path: 'setting-management',
    loadChildren: () => import('@abp/ng.setting-management').then(c => c.SettingManagementModule),
  },
];
