from google.protobuf.timestamp_pb2 import Timestamp
import address_book.addressbook_pb2 as addressbook_pb2


class AddressBook:
    def __init__(self):
        self.address_book = addressbook_pb2.AddressBook()

    def write_to_addressbook(self, name, id, email):
        person = addressbook_pb2.Person()
        person.name = name
        person.id = id
        person.email = email

        # set default number
        person.phones.add(number="9999999", type=addressbook_pb2.Person.PhoneType.MOBILE)
        person.phones.add(number="8888888", type=addressbook_pb2.Person.PhoneType.HOME)

        self.address_book.people.extend([person])

    def read_from_addressbook(self, name):
        for person in self.address_book.people:
            if person.name == name:
                print(person)


ab = AddressBook()
ab.write_to_addressbook("John", 123, "john@john.john")
ab.read_from_addressbook("John")