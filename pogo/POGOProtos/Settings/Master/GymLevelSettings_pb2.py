# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Settings/Master/GymLevelSettings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos/Settings/Master/GymLevelSettings.proto',
  package='POGOProtos.Settings.Master',
  syntax='proto3',
  serialized_pb=_b('\n1POGOProtos/Settings/Master/GymLevelSettings.proto\x12\x1aPOGOProtos.Settings.Master\"w\n\x10GymLevelSettings\x12\x1b\n\x13required_experience\x18\x01 \x03(\x05\x12\x14\n\x0cleader_slots\x18\x02 \x03(\x05\x12\x15\n\rtrainer_slots\x18\x03 \x03(\x05\x12\x19\n\x11search_roll_bonus\x18\x04 \x03(\x05\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GYMLEVELSETTINGS = _descriptor.Descriptor(
  name='GymLevelSettings',
  full_name='POGOProtos.Settings.Master.GymLevelSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='required_experience', full_name='POGOProtos.Settings.Master.GymLevelSettings.required_experience', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='leader_slots', full_name='POGOProtos.Settings.Master.GymLevelSettings.leader_slots', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trainer_slots', full_name='POGOProtos.Settings.Master.GymLevelSettings.trainer_slots', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='search_roll_bonus', full_name='POGOProtos.Settings.Master.GymLevelSettings.search_roll_bonus', index=3,
      number=4, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=81,
  serialized_end=200,
)

DESCRIPTOR.message_types_by_name['GymLevelSettings'] = _GYMLEVELSETTINGS

GymLevelSettings = _reflection.GeneratedProtocolMessageType('GymLevelSettings', (_message.Message,), dict(
  DESCRIPTOR = _GYMLEVELSETTINGS,
  __module__ = 'POGOProtos.Settings.Master.GymLevelSettings_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Settings.Master.GymLevelSettings)
  ))
_sym_db.RegisterMessage(GymLevelSettings)


# @@protoc_insertion_point(module_scope)
