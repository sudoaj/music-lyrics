import { Component, OnInit, Input} from '@angular/core';

@Component({
  selector: 'app-album-song-card',
  templateUrl: './album-song-card.component.html',
  styleUrls: ['./album-song-card.component.css']
})
export class AlbumSongCardComponent implements OnInit {

  @Input() albumSongNames:String | undefined;
  lyrics:string | undefined;
  constructor() {  
  }


  ngOnInit() {
  }

}
