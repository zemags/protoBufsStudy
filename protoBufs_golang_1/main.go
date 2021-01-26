package main

import (
	"fmt"

	simplepb "github.com/zemags/protoBufs_golang_1/src/simple"
)

func main() {
	doSimple()
}

func doSimple() {
	sm := simplepb.SimpleMessage{
		Id:         12345,
		IsSimple:   true,
		Name:       "My simple message",
		SampleList: []int32{1, 2, 3, 4, 5, 6, 7},
	}
	fmt.Println(sm)

	sm.Name = "Renamed name"
	fmt.Println(sm)

	fmt.Println(sm.GetId()) // 12345
}
