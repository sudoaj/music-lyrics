import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-song-lyrics',
  templateUrl: './home-page.component.html',
  styleUrls: ['./home-page.component.css']
})
export class HomePage implements OnInit {
  albumTitles = ["Scorpion", "Ayo", "Swifty", "Going Nuts"];
  source=["assets/img/dogs/image1.jpeg", "assets/img/dogs/image2.jpeg","assets/img/dogs/image3.jpeg"];
  artisteName=["Drake", "Cradi B", "Taylor Swift", "Y-Ceee"];
  
  constructor() { }

  ngOnInit() {
  }

}
