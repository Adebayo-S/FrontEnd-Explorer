describe("Address Book", function(){

    it("should be able to add a contact", function(){

        let addressBook = new AddressBook();
        let thisContact = new Contact("Samuel", "Adebayo", "07012345678", "1");

        addressBook.addContact(thisContact);
        expect(addressBook.getContact(0)).toBe(thisContact);
    });

    it("should be able to delete a contact", function() {
        let addressBook = new AddressBook();
        let thisContact = new Contact("Samuel", "Adebayo", "07012345678", "1");

        addressBook.addContact(thisContact);
        addressBook.deleteContact(0);
        expect(addressBook.getContact(0)).not.toBeDefined();
    })
});
