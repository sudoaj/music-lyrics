import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { LyricsPageComponent } from './lyrics-page.component';

describe('LyricsPageComponent', () => {
  let component: LyricsPageComponent;
  let fixture: ComponentFixture<LyricsPageComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ LyricsPageComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(LyricsPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
