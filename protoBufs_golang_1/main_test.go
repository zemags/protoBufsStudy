package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestDoSimple(t *testing.T) {
	type simpleMessageStruct struct {
		Id         int32
		IsSimple   bool
		Name       string
		SampleList []int32
	}

	expected := simpleMessageStruct{
		Id:         12345,
		IsSimple:   true,
		Name:       "Renamed name",
		SampleList: []int32{1, 2, 3, 4, 5, 6, 7},
	}

	sm := doSimple()
	result := simpleMessageStruct{
		Id:         sm.GetId(),
		IsSimple:   sm.GetIsSimple(),
		Name:       sm.GetName(),
		SampleList: sm.GetSampleList(),
	}
	assert.Equal(t, result, expected, "they should be equal")
}
