import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LayoutComponent } from './shared/layout/layout.component'
import { AppComponent } from './app.component'
import { HomePage } from './home/home-page/home-page.component'
import { LyricsPageComponent } from './lyrics/lyrics-page/lyrics-page.component'
import { VisualizePageComponent } from './visualize/visualize-page/visualize-page.component'



import { SongDetailsComponent } from './shared/components/song-details/song-details.component'


const routes: Routes = [
  {path: '', component: HomePage},
  {path: 'lyrics', component: LyricsPageComponent},
  {path: 'visualize', component: VisualizePageComponent},



  {path: 'anysong', component: SongDetailsComponent}
 
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
