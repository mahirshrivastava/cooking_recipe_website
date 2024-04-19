import { Component } from "@angular/core";

@Component({
    selector: 'greeting-app',
    templateUrl: './greeting.component.html',
    styleUrl: './greeting.component.css',
    standalone: true

})
export class GreetingComponent {
    title = "Greetings! Mahir"
}