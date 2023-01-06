class Customer {
  name: string;

  constructor(name: string) {
    this.name = name;
  }

  announce() {
    return "Hello, my name is " + this.name;
  }
}

let firstCustomer = new Customer("Allice");
let newMessage: string = firstCustomer.announce();
