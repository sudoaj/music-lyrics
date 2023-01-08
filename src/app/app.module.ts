import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeModule } from './home/home.module';
import {LyricsModule} from './lyrics/lyrics.module'
import {VisualizeModule} from './visualize/visualize.module'
import { SharedModule } from './shared/shared.module';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    HomeModule,
    SharedModule,
    BrowserModule,
    AppRoutingModule,
    LyricsModule,
    VisualizeModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
