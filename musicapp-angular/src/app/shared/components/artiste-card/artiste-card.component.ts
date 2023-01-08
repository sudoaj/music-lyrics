import { Component, OnInit, Input} from '@angular/core';

@Component({
  selector: 'app-artiste-card',
  templateUrl: './artiste-card.component.html',
  styleUrls: ['./artiste-card.component.css']
})
export class ArtisteCardComponent implements OnInit {
  @Input() artisteAvartar : string | undefined;
  @Input() artisteName : string | undefined;

  constructor() {
   }

  ngOnInit() {
  }

}
