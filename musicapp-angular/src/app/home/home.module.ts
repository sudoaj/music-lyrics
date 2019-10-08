import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SongLyricsComponent } from './song-lyrics/song-lyrics.component';
import { SharedModule } from '../shared/shared.module'

@NgModule({
  declarations: [
    SongLyricsComponent
  ],
  imports: [
    CommonModule,
    SharedModule,
    
  ],

  exports:[
    SongLyricsComponent
  ]
})
export class HomeModule { }
