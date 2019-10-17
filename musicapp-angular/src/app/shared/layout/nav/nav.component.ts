import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrls: ['./nav.component.css']
})
export class NavComponent implements OnInit {

  constructor(private router: Router) { }

  ngOnInit() {
  }
  gotoHomePage() : void{
    
    this.router.navigate(['/'])

    }
  gotoLyricsPage() : void{
    
    this.router.navigate(['/lyrics'])

    }

    gotoVisualizePage() : void{
    
      this.router.navigate(['/visualize'])
  
      }

}
