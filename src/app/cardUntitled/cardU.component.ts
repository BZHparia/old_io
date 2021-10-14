import { Component, Input, OnInit, Output, EventEmitter, Inject } from '@angular/core';
import {MatIconModule} from '@angular/material/icon';
import { DOCUMENT } from '@angular/common';

@Component({
  selector: 'app-cardU',
  templateUrl: './cardU.component.html',
  styleUrls: ['./cardU.component.scss']
})
export class CardUComponent implements OnInit {

  @Input() description: string;
  @Input() img: string;

  @Output() linkEvent =  new EventEmitter<string>();
  @Input() allLinks: string[];
  @Input() allNames: string[];

  @Input() setLink: string;

  constructor(@Inject(DOCUMENT) private document: Document) {
    this.description = "";
    this.img = 'assets/img/blank.png';
    this.allLinks = [];
    this.allNames = [];
    this.setLink = "";
   }

  ngOnInit(): void {
  }

  sendLink(index: number) {
    this.linkEvent.emit(this.allLinks[index])
  }

  goToUrl(link: string | undefined) {
    window.open(
      link,
      '_blank'
    );
  }
}
