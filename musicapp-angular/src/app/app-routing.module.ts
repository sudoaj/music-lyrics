import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LayoutComponent } from './shared/layout/layout.component'
import { AppComponent } from './app.component'
import { SongLyricsComponent } from './home/song-lyrics/song-lyrics.component'

const routes: Routes = [
  {path: '', component: SongLyricsComponent},
];

// const routes: Routes = [
//   { path: ' ',
//     loadChildren: () => import('./home/home.module').then(m => m.HomeModule) }
//   ];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
