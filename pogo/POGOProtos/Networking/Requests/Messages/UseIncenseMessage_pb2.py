# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Networking/Requests/Messages/UseIncenseMessage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from POGOProtos.Inventory import ItemId_pb2 as POGOProtos_dot_Inventory_dot_ItemId__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos/Networking/Requests/Messages/UseIncenseMessage.proto',
  package='POGOProtos.Networking.Requests.Messages',
  syntax='proto3',
  serialized_pb=_b('\n?POGOProtos/Networking/Requests/Messages/UseIncenseMessage.proto\x12\'POGOProtos.Networking.Requests.Messages\x1a!POGOProtos/Inventory/ItemId.proto\"G\n\x11UseIncenseMessage\x12\x32\n\x0cincense_type\x18\x01 \x01(\x0e\x32\x1c.POGOProtos.Inventory.ItemIdb\x06proto3')
  ,
  dependencies=[POGOProtos_dot_Inventory_dot_ItemId__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_USEINCENSEMESSAGE = _descriptor.Descriptor(
  name='UseIncenseMessage',
  full_name='POGOProtos.Networking.Requests.Messages.UseIncenseMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='incense_type', full_name='POGOProtos.Networking.Requests.Messages.UseIncenseMessage.incense_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
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
  serialized_start=143,
  serialized_end=214,
)

_USEINCENSEMESSAGE.fields_by_name['incense_type'].enum_type = POGOProtos_dot_Inventory_dot_ItemId__pb2._ITEMID
DESCRIPTOR.message_types_by_name['UseIncenseMessage'] = _USEINCENSEMESSAGE

UseIncenseMessage = _reflection.GeneratedProtocolMessageType('UseIncenseMessage', (_message.Message,), dict(
  DESCRIPTOR = _USEINCENSEMESSAGE,
  __module__ = 'POGOProtos.Networking.Requests.Messages.UseIncenseMessage_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Networking.Requests.Messages.UseIncenseMessage)
  ))
_sym_db.RegisterMessage(UseIncenseMessage)


# @@protoc_insertion_point(module_scope)
