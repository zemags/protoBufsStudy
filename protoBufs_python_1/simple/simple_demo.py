import simple.simple_pb2 as simple_pb2

simple_message = simple_pb2.SimpleMessage()
simple_message.id = 123
simple_message.is_simple = True # by default false and now showing if print it
simple_message.name = "Simple message here"
sample_list = simple_message.sample_list
sample_list.append(2)

with open("simple.bin", "wb") as f:
    byte_as_string = simple_message.SerializeToString() # bytestring
    f.write(byte_as_string)

with open("simple.bin", "rb") as f:
    simple_message_read = simple_pb2.SimpleMessage().FromString(f.read())

print(simple_message_read)
print(simple_message_read.is_simple)