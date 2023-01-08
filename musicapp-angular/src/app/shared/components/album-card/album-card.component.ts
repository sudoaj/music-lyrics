import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-album-card',
  templateUrl: './album-card.component.html',
  styleUrls: ['./album-card.component.css']
})
export class AlbumCardComponent implements OnInit { 
  @Input() albumTitles: String | undefined;
  @Input() albumArtiste: String | undefined;

  albumSongName = ["needed me", "gods plan", "champion", "who's the boss now"];
  
  constructor() { 
    
  }

  ngOnInit() {
  }

}
