import { Component, ViewChild, AfterViewInit, Inject } from '@angular/core';
import { Router } from '@angular/router';
import { DOCUMENT } from '@angular/common';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'angular-electron';

  link: string ="";

  constructor(@Inject(DOCUMENT) private document: Document) {
    
  }
  
  receiveLink($event: string) {
    this.link = $event;
  }

  goToUrl(link: string | undefined) {
    window.open(
      link,
      '_blank'
    );
  }
}
