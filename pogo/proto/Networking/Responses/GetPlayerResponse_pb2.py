# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Networking/Responses/GetPlayerResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from Data import PlayerData_pb2 as Data_dot_PlayerData__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Networking/Responses/GetPlayerResponse.proto',
  package='POGOProtos.Networking.Responses',
  syntax='proto3',
  serialized_pb=_b('\n,Networking/Responses/GetPlayerResponse.proto\x12\x1fPOGOProtos.Networking.Responses\x1a\x15\x44\x61ta/PlayerData.proto\"V\n\x11GetPlayerResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x30\n\x0bplayer_data\x18\x02 \x01(\x0b\x32\x1b.POGOProtos.Data.PlayerDatab\x06proto3')
  ,
  dependencies=[Data_dot_PlayerData__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GETPLAYERRESPONSE = _descriptor.Descriptor(
  name='GetPlayerResponse',
  full_name='POGOProtos.Networking.Responses.GetPlayerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='POGOProtos.Networking.Responses.GetPlayerResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_data', full_name='POGOProtos.Networking.Responses.GetPlayerResponse.player_data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=104,
  serialized_end=190,
)

_GETPLAYERRESPONSE.fields_by_name['player_data'].message_type = Data_dot_PlayerData__pb2._PLAYERDATA
DESCRIPTOR.message_types_by_name['GetPlayerResponse'] = _GETPLAYERRESPONSE

GetPlayerResponse = _reflection.GeneratedProtocolMessageType('GetPlayerResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETPLAYERRESPONSE,
  __module__ = 'Networking.Responses.GetPlayerResponse_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Networking.Responses.GetPlayerResponse)
  ))
_sym_db.RegisterMessage(GetPlayerResponse)


# @@protoc_insertion_point(module_scope)
