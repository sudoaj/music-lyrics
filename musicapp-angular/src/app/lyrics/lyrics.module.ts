import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { LyricsPageComponent } from './lyrics-page/lyrics-page.component';
import { SharedModule } from '../shared/shared.module'



@NgModule({
  declarations: [
    LyricsPageComponent
  ],

  imports: [
    CommonModule,
    SharedModule
  ],
  exports:[
    LyricsPageComponent
  ]
})
export class LyricsModule { }
