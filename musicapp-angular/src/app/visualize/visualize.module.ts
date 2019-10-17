import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { VisualizePageComponent } from './visualize-page/visualize-page.component';
import { SharedModule } from '../shared/shared.module';



@NgModule({
  declarations: [
    VisualizePageComponent
  ],
  imports: [
    CommonModule,
    SharedModule
  ],

  exports:[
    VisualizePageComponent
  ]
})
export class VisualizeModule { }
