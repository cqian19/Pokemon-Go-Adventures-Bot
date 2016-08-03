# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Networking/Responses/SetContactSettingsResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from POGOProtos.Data import PlayerData_pb2 as POGOProtos_dot_Data_dot_PlayerData__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos/Networking/Responses/SetContactSettingsResponse.proto',
  package='POGOProtos.Networking.Responses',
  syntax='proto3',
  serialized_pb=_b('\n@POGOProtos/Networking/Responses/SetContactSettingsResponse.proto\x12\x1fPOGOProtos.Networking.Responses\x1a POGOProtos/Data/PlayerData.proto\"\xd1\x01\n\x1aSetContactSettingsResponse\x12R\n\x06status\x18\x01 \x01(\x0e\x32\x42.POGOProtos.Networking.Responses.SetContactSettingsResponse.Status\x12\x30\n\x0bplayer_data\x18\x02 \x01(\x0b\x32\x1b.POGOProtos.Data.PlayerData\"-\n\x06Status\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x0b\n\x07\x46\x41ILURE\x10\x02\x62\x06proto3')
  ,
  dependencies=[POGOProtos_dot_Data_dot_PlayerData__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_SETCONTACTSETTINGSRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='POGOProtos.Networking.Responses.SetContactSettingsResponse.Status',
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
      name='FAILURE', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=300,
  serialized_end=345,
)
_sym_db.RegisterEnumDescriptor(_SETCONTACTSETTINGSRESPONSE_STATUS)


_SETCONTACTSETTINGSRESPONSE = _descriptor.Descriptor(
  name='SetContactSettingsResponse',
  full_name='POGOProtos.Networking.Responses.SetContactSettingsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='POGOProtos.Networking.Responses.SetContactSettingsResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_data', full_name='POGOProtos.Networking.Responses.SetContactSettingsResponse.player_data', index=1,
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
    _SETCONTACTSETTINGSRESPONSE_STATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=136,
  serialized_end=345,
)

_SETCONTACTSETTINGSRESPONSE.fields_by_name['status'].enum_type = _SETCONTACTSETTINGSRESPONSE_STATUS
_SETCONTACTSETTINGSRESPONSE.fields_by_name['player_data'].message_type = POGOProtos_dot_Data_dot_PlayerData__pb2._PLAYERDATA
_SETCONTACTSETTINGSRESPONSE_STATUS.containing_type = _SETCONTACTSETTINGSRESPONSE
DESCRIPTOR.message_types_by_name['SetContactSettingsResponse'] = _SETCONTACTSETTINGSRESPONSE

SetContactSettingsResponse = _reflection.GeneratedProtocolMessageType('SetContactSettingsResponse', (_message.Message,), dict(
  DESCRIPTOR = _SETCONTACTSETTINGSRESPONSE,
  __module__ = 'POGOProtos.Networking.Responses.SetContactSettingsResponse_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Networking.Responses.SetContactSettingsResponse)
  ))
_sym_db.RegisterMessage(SetContactSettingsResponse)


# @@protoc_insertion_point(module_scope)
