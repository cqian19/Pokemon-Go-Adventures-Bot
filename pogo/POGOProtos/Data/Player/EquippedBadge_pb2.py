# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Data/Player/EquippedBadge.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from POGOProtos.Enums import BadgeType_pb2 as POGOProtos_dot_Enums_dot_BadgeType__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos/Data/Player/EquippedBadge.proto',
  package='POGOProtos.Data.Player',
  syntax='proto3',
  serialized_pb=_b('\n*POGOProtos/Data/Player/EquippedBadge.proto\x12\x16POGOProtos.Data.Player\x1a POGOProtos/Enums/BadgeType.proto\"\x7f\n\rEquippedBadge\x12/\n\nbadge_type\x18\x01 \x01(\x0e\x32\x1b.POGOProtos.Enums.BadgeType\x12\r\n\x05level\x18\x02 \x01(\x05\x12.\n&next_equip_change_allowed_timestamp_ms\x18\x03 \x01(\x03\x62\x06proto3')
  ,
  dependencies=[POGOProtos_dot_Enums_dot_BadgeType__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_EQUIPPEDBADGE = _descriptor.Descriptor(
  name='EquippedBadge',
  full_name='POGOProtos.Data.Player.EquippedBadge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='badge_type', full_name='POGOProtos.Data.Player.EquippedBadge.badge_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='POGOProtos.Data.Player.EquippedBadge.level', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_equip_change_allowed_timestamp_ms', full_name='POGOProtos.Data.Player.EquippedBadge.next_equip_change_allowed_timestamp_ms', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_end=231,
)

_EQUIPPEDBADGE.fields_by_name['badge_type'].enum_type = POGOProtos_dot_Enums_dot_BadgeType__pb2._BADGETYPE
DESCRIPTOR.message_types_by_name['EquippedBadge'] = _EQUIPPEDBADGE

EquippedBadge = _reflection.GeneratedProtocolMessageType('EquippedBadge', (_message.Message,), dict(
  DESCRIPTOR = _EQUIPPEDBADGE,
  __module__ = 'POGOProtos.Data.Player.EquippedBadge_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Data.Player.EquippedBadge)
  ))
_sym_db.RegisterMessage(EquippedBadge)


# @@protoc_insertion_point(module_scope)
