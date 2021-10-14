import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CardUComponent } from './cardU.component';

describe('CardUComponent', () => {
  let component: CardUComponent;
  let fixture: ComponentFixture<CardUComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CardUComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CardUComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
