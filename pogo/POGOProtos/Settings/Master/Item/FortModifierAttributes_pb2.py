# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Settings/Master/Item/FortModifierAttributes.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos/Settings/Master/Item/FortModifierAttributes.proto',
  package='POGOProtos.Settings.Master.Item',
  syntax='proto3',
  serialized_pb=_b('\n<POGOProtos/Settings/Master/Item/FortModifierAttributes.proto\x12\x1fPOGOProtos.Settings.Master.Item\"b\n\x16\x46ortModifierAttributes\x12!\n\x19modifier_lifetime_seconds\x18\x01 \x01(\x05\x12%\n\x1dtroy_disk_num_pokemon_spawned\x18\x02 \x01(\x05\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_FORTMODIFIERATTRIBUTES = _descriptor.Descriptor(
  name='FortModifierAttributes',
  full_name='POGOProtos.Settings.Master.Item.FortModifierAttributes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='modifier_lifetime_seconds', full_name='POGOProtos.Settings.Master.Item.FortModifierAttributes.modifier_lifetime_seconds', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='troy_disk_num_pokemon_spawned', full_name='POGOProtos.Settings.Master.Item.FortModifierAttributes.troy_disk_num_pokemon_spawned', index=1,
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
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=97,
  serialized_end=195,
)

DESCRIPTOR.message_types_by_name['FortModifierAttributes'] = _FORTMODIFIERATTRIBUTES

FortModifierAttributes = _reflection.GeneratedProtocolMessageType('FortModifierAttributes', (_message.Message,), dict(
  DESCRIPTOR = _FORTMODIFIERATTRIBUTES,
  __module__ = 'POGOProtos.Settings.Master.Item.FortModifierAttributes_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Settings.Master.Item.FortModifierAttributes)
  ))
_sym_db.RegisterMessage(FortModifierAttributes)


# @@protoc_insertion_point(module_scope)
