# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Networking/Requests/Messages/GetPlayerMessage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos/Networking/Requests/Messages/GetPlayerMessage.proto',
  package='POGOProtos.Networking.Requests.Messages',
  syntax='proto3',
  serialized_pb=_b('\n>POGOProtos/Networking/Requests/Messages/GetPlayerMessage.proto\x12\'POGOProtos.Networking.Requests.Messages\"\x12\n\x10GetPlayerMessageb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GETPLAYERMESSAGE = _descriptor.Descriptor(
  name='GetPlayerMessage',
  full_name='POGOProtos.Networking.Requests.Messages.GetPlayerMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=107,
  serialized_end=125,
)

DESCRIPTOR.message_types_by_name['GetPlayerMessage'] = _GETPLAYERMESSAGE

GetPlayerMessage = _reflection.GeneratedProtocolMessageType('GetPlayerMessage', (_message.Message,), dict(
  DESCRIPTOR = _GETPLAYERMESSAGE,
  __module__ = 'POGOProtos.Networking.Requests.Messages.GetPlayerMessage_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Networking.Requests.Messages.GetPlayerMessage)
  ))
_sym_db.RegisterMessage(GetPlayerMessage)


# @@protoc_insertion_point(module_scope)
