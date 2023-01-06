"use strict";
class Customer {
    constructor(name) {
        this.name = name;
    }
    announce() {
        return "Hello, my name is " + this.name;
    }
}
let firstCustomer = new Customer("Allice");
let newMessage = firstCustomer.announce();
