# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Networking/Responses/ReleasePokemonResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos/Networking/Responses/ReleasePokemonResponse.proto',
  package='POGOProtos.Networking.Responses',
  syntax='proto3',
  serialized_pb=_b('\n<POGOProtos/Networking/Responses/ReleasePokemonResponse.proto\x12\x1fPOGOProtos.Networking.Responses\"\xdd\x01\n\x16ReleasePokemonResponse\x12N\n\x06result\x18\x01 \x01(\x0e\x32>.POGOProtos.Networking.Responses.ReleasePokemonResponse.Result\x12\x15\n\rcandy_awarded\x18\x02 \x01(\x05\"\\\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x14\n\x10POKEMON_DEPLOYED\x10\x02\x12\n\n\x06\x46\x41ILED\x10\x03\x12\x18\n\x14\x45RROR_POKEMON_IS_EGG\x10\x04\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_RELEASEPOKEMONRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='POGOProtos.Networking.Responses.ReleasePokemonResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEMON_DEPLOYED', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_POKEMON_IS_EGG', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=227,
  serialized_end=319,
)
_sym_db.RegisterEnumDescriptor(_RELEASEPOKEMONRESPONSE_RESULT)


_RELEASEPOKEMONRESPONSE = _descriptor.Descriptor(
  name='ReleasePokemonResponse',
  full_name='POGOProtos.Networking.Responses.ReleasePokemonResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='POGOProtos.Networking.Responses.ReleasePokemonResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='candy_awarded', full_name='POGOProtos.Networking.Responses.ReleasePokemonResponse.candy_awarded', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RELEASEPOKEMONRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=98,
  serialized_end=319,
)

_RELEASEPOKEMONRESPONSE.fields_by_name['result'].enum_type = _RELEASEPOKEMONRESPONSE_RESULT
_RELEASEPOKEMONRESPONSE_RESULT.containing_type = _RELEASEPOKEMONRESPONSE
DESCRIPTOR.message_types_by_name['ReleasePokemonResponse'] = _RELEASEPOKEMONRESPONSE

ReleasePokemonResponse = _reflection.GeneratedProtocolMessageType('ReleasePokemonResponse', (_message.Message,), dict(
  DESCRIPTOR = _RELEASEPOKEMONRESPONSE,
  __module__ = 'POGOProtos.Networking.Responses.ReleasePokemonResponse_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Networking.Responses.ReleasePokemonResponse)
  ))
_sym_db.RegisterMessage(ReleasePokemonResponse)


# @@protoc_insertion_point(module_scope)
