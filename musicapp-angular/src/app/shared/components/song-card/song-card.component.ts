import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-song-card',
  templateUrl: './song-card.component.html',
  styleUrls: ['./song-card.component.css']
})
export class SongCardComponent implements OnInit {
  song:String ;
  lyrics:string;
  constructor() { 
    this.song= "Gods Plan";
    this.lyrics= "Bad things\n  It's a lot of bad things\n That they wishin' and wishin' and wishin' and wishin'"
   
    
  }

  ngOnInit() {
  }

}





