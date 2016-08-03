# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Data/PokedexEntry.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from POGOProtos.Enums import PokemonId_pb2 as POGOProtos_dot_Enums_dot_PokemonId__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos/Data/PokedexEntry.proto',
  package='POGOProtos.Data',
  syntax='proto3',
  serialized_pb=_b('\n\"POGOProtos/Data/PokedexEntry.proto\x12\x0fPOGOProtos.Data\x1a POGOProtos/Enums/PokemonId.proto\"\xac\x01\n\x0cPokedexEntry\x12/\n\npokemon_id\x18\x01 \x01(\x0e\x32\x1b.POGOProtos.Enums.PokemonId\x12\x19\n\x11times_encountered\x18\x02 \x01(\x05\x12\x16\n\x0etimes_captured\x18\x03 \x01(\x05\x12\x1e\n\x16\x65volution_stone_pieces\x18\x04 \x01(\x05\x12\x18\n\x10\x65volution_stones\x18\x05 \x01(\x05\x62\x06proto3')
  ,
  dependencies=[POGOProtos_dot_Enums_dot_PokemonId__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_POKEDEXENTRY = _descriptor.Descriptor(
  name='PokedexEntry',
  full_name='POGOProtos.Data.PokedexEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pokemon_id', full_name='POGOProtos.Data.PokedexEntry.pokemon_id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='times_encountered', full_name='POGOProtos.Data.PokedexEntry.times_encountered', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='times_captured', full_name='POGOProtos.Data.PokedexEntry.times_captured', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='evolution_stone_pieces', full_name='POGOProtos.Data.PokedexEntry.evolution_stone_pieces', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='evolution_stones', full_name='POGOProtos.Data.PokedexEntry.evolution_stones', index=4,
      number=5, type=5, cpp_type=1, label=1,
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
  serialized_start=90,
  serialized_end=262,
)

_POKEDEXENTRY.fields_by_name['pokemon_id'].enum_type = POGOProtos_dot_Enums_dot_PokemonId__pb2._POKEMONID
DESCRIPTOR.message_types_by_name['PokedexEntry'] = _POKEDEXENTRY

PokedexEntry = _reflection.GeneratedProtocolMessageType('PokedexEntry', (_message.Message,), dict(
  DESCRIPTOR = _POKEDEXENTRY,
  __module__ = 'POGOProtos.Data.PokedexEntry_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Data.PokedexEntry)
  ))
_sym_db.RegisterMessage(PokedexEntry)


# @@protoc_insertion_point(module_scope)
