package main

import (
	"errors"
	"fmt"
	"log"
	addressbookpb "protoBufs_practice_1/src/addressbook"

	timestamppb "google.golang.org/protobuf/types/known/timestamppb"
)

func main() {
	addressBook := &addressbookpb.AddressBook{
		People: []*addressbookpb.Person{},
	}
	person1 := createPerson("John", 123, "john123@123.com")
	person2 := createPerson("kikflip", 456, "kikflip@kickflip.com")
	writeToAddressBook(person1, addressBook)
	writeToAddressBook(person2, addressBook)
	person, err := readFromAddressBook("John", addressBook)
	if err != nil {
		log.Fatalln(err)
	}
	fmt.Println(person)
}

func writeToAddressBook(p *addressbookpb.Person, ab *addressbookpb.AddressBook) *addressbookpb.AddressBook {
	ab.People = append(ab.People, p)
	return ab
}

func readFromAddressBook(name string, ab *addressbookpb.AddressBook) (*addressbookpb.Person, error) {
	for _, person := range ab.People {
		if person.Name == name {
			return person, nil
		}
	}
	return &addressbookpb.Person{}, errors.New("Can't find person")
}

func createPerson(name string, id int32, email string) *addressbookpb.Person {
	p := addressbookpb.Person{
		Name:  name,
		Id:    id,
		Email: email,
		Phones: []*addressbookpb.Person_PhoneNumber{
			&addressbookpb.Person_PhoneNumber{
				Number: "99999999",
				Type:   addressbookpb.Person_MOBILE,
			},
			&addressbookpb.Person_PhoneNumber{
				Number: "88888888",
				Type:   addressbookpb.Person_HOME,
			},
		},
		LastUpdated: &timestamppb.Timestamp{
			Seconds: 1000000,
		},
	}
	return &p
}
