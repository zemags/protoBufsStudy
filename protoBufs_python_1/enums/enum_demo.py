import enums.enum_example_pb2 as enum_example_pb2

enum_message = enum_example_pb2.EnumMessage()
enum_message.id = 123
enum_message.day_of_the_week = enum_example_pb2.monday

print(enum_message)
print(enum_message.day_of_the_week) # 1
