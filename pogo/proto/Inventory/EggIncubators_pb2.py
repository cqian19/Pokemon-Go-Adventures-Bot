# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Inventory/EggIncubators.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from Inventory import EggIncubator_pb2 as Inventory_dot_EggIncubator__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Inventory/EggIncubators.proto',
  package='POGOProtos.Inventory',
  syntax='proto3',
  serialized_pb=_b('\n\x1dInventory/EggIncubators.proto\x12\x14POGOProtos.Inventory\x1a\x1cInventory/EggIncubator.proto\"J\n\rEggIncubators\x12\x39\n\regg_incubator\x18\x01 \x01(\x0b\x32\".POGOProtos.Inventory.EggIncubatorb\x06proto3')
  ,
  dependencies=[Inventory_dot_EggIncubator__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_EGGINCUBATORS = _descriptor.Descriptor(
  name='EggIncubators',
  full_name='POGOProtos.Inventory.EggIncubators',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='egg_incubator', full_name='POGOProtos.Inventory.EggIncubators.egg_incubator', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=85,
  serialized_end=159,
)

_EGGINCUBATORS.fields_by_name['egg_incubator'].message_type = Inventory_dot_EggIncubator__pb2._EGGINCUBATOR
DESCRIPTOR.message_types_by_name['EggIncubators'] = _EGGINCUBATORS

EggIncubators = _reflection.GeneratedProtocolMessageType('EggIncubators', (_message.Message,), dict(
  DESCRIPTOR = _EGGINCUBATORS,
  __module__ = 'Inventory.EggIncubators_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Inventory.EggIncubators)
  ))
_sym_db.RegisterMessage(EggIncubators)


# @@protoc_insertion_point(module_scope)
