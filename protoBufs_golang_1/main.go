package main

import (
	"fmt"
	"io/ioutil"
	"log"

	simplepb "github.com/zemags/protoBufs_golang_1/src/simple"
	"google.golang.org/protobuf/encoding/protojson"
	"google.golang.org/protobuf/proto"
)

func main() {
	sm := doSimple()
	readWriteFile(sm)
	readWriteJSON(sm)
}

func toJSON(pb proto.Message) string {
	marshaler := protojson.MarshalOptions{}
	out, err := marshaler.Marshal(pb)
	if err != nil {
		log.Fatalln("Can't convert to JSON", err)
		return ""
	}
	return string(out)
}

func fromJSON(in []byte, pb proto.Message) {
	if err := protojson.Unmarshal(in, pb); err != nil {
		log.Fatalln("Can't unmarshal json")
	}
}

func readWriteJSON(sm proto.Message) {
	smAsString := toJSON(sm)
	fmt.Println(smAsString)

	sm2 := &simplepb.SimpleMessage{}
	fromJSON([]byte(smAsString), sm2)
	fmt.Println("Read from json")
}

func readWriteFile(sm proto.Message) {
	writeToFile("simple.bin", sm)
	sm2 := &simplepb.SimpleMessage{}
	readFromFile("simple.bin", sm2)
	fmt.Println(sm2)
}

func writeToFile(fname string, pb proto.Message) error {
	out, err := proto.Marshal(pb)

	if err != nil {
		log.Fatalln("Can't serialise to bytes", err)
		return err
	}

	if err := ioutil.WriteFile(fname, out, 0644); err != nil {
		log.Fatalln("Can't write to file", err)
		return err
	}

	fmt.Println("Data has been written.")
	return nil
}

func readFromFile(fname string, pb proto.Message) error {
	data, err := ioutil.ReadFile(fname)
	if err != nil {
		log.Fatalln("Can't read from file", err)
	}

	if err := proto.Unmarshal(data, pb); err != nil {
		log.Fatalln("Can't read from file", err)
	}
	fmt.Println("Data has been readed.")
	return nil
}

func doSimple() *simplepb.SimpleMessage {
	sm := simplepb.SimpleMessage{
		Id:         12345,
		IsSimple:   true,
		Name:       "My simple message",
		SampleList: []int32{1, 2, 3, 4, 5, 6, 7},
	}
	sm.Name = "Renamed name"
	return &sm
}
