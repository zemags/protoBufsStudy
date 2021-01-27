import complex.complex_pb2 as complex_pb2

complex_message = complex_pb2.ComplexMessage()
complex_message.one_dummy.id = 123
complex_message.one_dummy.name = "This is dummy message"

first_multiple_dummy = complex_message.multiple_dummy.add()
first_multiple_dummy.id = 345
first_multiple_dummy.name = "First element of array"

complex_message.multiple_dummy.add(id=567, name="Second element of array")

third_dummy_message = complex_pb2.DummyMessage()
third_dummy_message.id = 999
third_dummy_message.name = "abc"
complex_message.multiple_dummy.extend([third_dummy_message])

third_dummy_message.id = 111
print(third_dummy_message)

# print(complex_message)