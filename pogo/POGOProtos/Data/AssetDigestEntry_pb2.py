# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Data/AssetDigestEntry.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos/Data/AssetDigestEntry.proto',
  package='POGOProtos.Data',
  syntax='proto3',
  serialized_pb=_b('\n&POGOProtos/Data/AssetDigestEntry.proto\x12\x0fPOGOProtos.Data\"w\n\x10\x41ssetDigestEntry\x12\x10\n\x08\x61sset_id\x18\x01 \x01(\t\x12\x13\n\x0b\x62undle_name\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\x03\x12\x10\n\x08\x63hecksum\x18\x04 \x01(\r\x12\x0c\n\x04size\x18\x05 \x01(\x05\x12\x0b\n\x03key\x18\x06 \x01(\x0c\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ASSETDIGESTENTRY = _descriptor.Descriptor(
  name='AssetDigestEntry',
  full_name='POGOProtos.Data.AssetDigestEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='asset_id', full_name='POGOProtos.Data.AssetDigestEntry.asset_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bundle_name', full_name='POGOProtos.Data.AssetDigestEntry.bundle_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='POGOProtos.Data.AssetDigestEntry.version', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='checksum', full_name='POGOProtos.Data.AssetDigestEntry.checksum', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='size', full_name='POGOProtos.Data.AssetDigestEntry.size', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='key', full_name='POGOProtos.Data.AssetDigestEntry.key', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=59,
  serialized_end=178,
)

DESCRIPTOR.message_types_by_name['AssetDigestEntry'] = _ASSETDIGESTENTRY

AssetDigestEntry = _reflection.GeneratedProtocolMessageType('AssetDigestEntry', (_message.Message,), dict(
  DESCRIPTOR = _ASSETDIGESTENTRY,
  __module__ = 'POGOProtos.Data.AssetDigestEntry_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Data.AssetDigestEntry)
  ))
_sym_db.RegisterMessage(AssetDigestEntry)


# @@protoc_insertion_point(module_scope)
