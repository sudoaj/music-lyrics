import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { LayoutComponent } from './layout/layout.component';
import { NavComponent } from './layout/nav/nav.component';
import { HeaderComponent } from './layout/header/header.component';
import { SongCardComponent } from './components/song-card/song-card.component';
import { AppRoutingModule } from '../app-routing.module';
import { AlbumCardComponent } from './components/album-card/album-card.component';
import { SongDetailsComponent } from './components/song-details/song-details.component';
import { AlbumSongCardComponent } from './components/album-song-card/album-song-card.component';
import { ArtisteCardComponent } from './components/artiste-card/artiste-card.component'



@NgModule({
  declarations: [
    LayoutComponent,
    NavComponent,
    HeaderComponent,
    SongCardComponent,
    AlbumCardComponent,
    SongDetailsComponent,
    AlbumSongCardComponent,
    ArtisteCardComponent
  ],
  imports: [
    CommonModule,
    AppRoutingModule
  ],
  exports: [
    LayoutComponent,
    NavComponent,
    HeaderComponent,
    SongCardComponent,
    AlbumCardComponent,
    ArtisteCardComponent
  ]
})
export class SharedModule { }
