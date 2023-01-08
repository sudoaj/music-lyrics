import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-album-card',
  templateUrl: './album-card.component.html',
  styleUrls: ['./album-card.component.css']
})
export class AlbumCardComponent implements OnInit { 
  @Input() albumTitles: String;
  @Input() albumArtiste: String;

  albumSongName = ["needed me", "gods plan", "champion", "who's the boss now"];
  
  constructor() { 
    
  }
2
  ngOnInit() {
  }

}
