describe("Address Book", function(){
	let addressBook;
	let thisContact;

	//before each spec do this
	beforeEach(function(){
		addressBook = new AddressBook();
		thisContact = new Contact();
	});

	it("should be able to add a contact", function(){
		addressBook.addContact(thisContact);

		expect(addressBook.getContact(0)).toBe(thisContact);
	});

	it("should be able to delete a contact", function() {
		addressBook.addContact(thisContact);
		addressBook.deleteContact(0);

		expect(addressBook.getContact(0)).not.toBeDefined();
	})
});

//in this case, the expect is running before the async operation completes
//so this spec will fail. Unless we use the beforeEach and
// done callback argument

describe('Async Address Book', function() {
	let addressBook = new AddressBook();

	//this will signal to the framework that our async function
	//is done
	beforeEach(function(done) {
		addressBook.getInitialContacts(function() {
			done();
		});
	});

	it('should grab initial contacts', function(done) {
		expect(addressBook.initialComplete).toBe(true);
		done(); //use this to signal that this function relies on the beforeEach exec
	});
});
