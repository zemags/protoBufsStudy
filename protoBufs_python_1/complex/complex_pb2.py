# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: complex.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='complex.proto',
  package='example.complex',
  syntax='proto3',
  serialized_options=b'Z\tcomplexpb',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rcomplex.proto\x12\x0f\x65xample.complex\"y\n\x0e\x43omplexMessage\x12\x30\n\tone_dummy\x18\x02 \x01(\x0b\x32\x1d.example.complex.DummyMessage\x12\x35\n\x0emultiple_dummy\x18\x03 \x03(\x0b\x32\x1d.example.complex.DummyMessage\"(\n\x0c\x44ummyMessage\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\tB\x0bZ\tcomplexpbb\x06proto3'
)




_COMPLEXMESSAGE = _descriptor.Descriptor(
  name='ComplexMessage',
  full_name='example.complex.ComplexMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='one_dummy', full_name='example.complex.ComplexMessage.one_dummy', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='multiple_dummy', full_name='example.complex.ComplexMessage.multiple_dummy', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=34,
  serialized_end=155,
)


_DUMMYMESSAGE = _descriptor.Descriptor(
  name='DummyMessage',
  full_name='example.complex.DummyMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='example.complex.DummyMessage.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='example.complex.DummyMessage.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=157,
  serialized_end=197,
)

_COMPLEXMESSAGE.fields_by_name['one_dummy'].message_type = _DUMMYMESSAGE
_COMPLEXMESSAGE.fields_by_name['multiple_dummy'].message_type = _DUMMYMESSAGE
DESCRIPTOR.message_types_by_name['ComplexMessage'] = _COMPLEXMESSAGE
DESCRIPTOR.message_types_by_name['DummyMessage'] = _DUMMYMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ComplexMessage = _reflection.GeneratedProtocolMessageType('ComplexMessage', (_message.Message,), {
  'DESCRIPTOR' : _COMPLEXMESSAGE,
  '__module__' : 'complex_pb2'
  # @@protoc_insertion_point(class_scope:example.complex.ComplexMessage)
  })
_sym_db.RegisterMessage(ComplexMessage)

DummyMessage = _reflection.GeneratedProtocolMessageType('DummyMessage', (_message.Message,), {
  'DESCRIPTOR' : _DUMMYMESSAGE,
  '__module__' : 'complex_pb2'
  # @@protoc_insertion_point(class_scope:example.complex.DummyMessage)
  })
_sym_db.RegisterMessage(DummyMessage)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
