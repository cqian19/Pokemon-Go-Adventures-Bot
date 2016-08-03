# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Data/Gym/GymMembership.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from POGOProtos.Data import PokemonData_pb2 as POGOProtos_dot_Data_dot_PokemonData__pb2
from POGOProtos.Data.Player import PlayerPublicProfile_pb2 as POGOProtos_dot_Data_dot_Player_dot_PlayerPublicProfile__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos/Data/Gym/GymMembership.proto',
  package='POGOProtos.Data.Gym',
  syntax='proto3',
  serialized_pb=_b('\n\'POGOProtos/Data/Gym/GymMembership.proto\x12\x13POGOProtos.Data.Gym\x1a!POGOProtos/Data/PokemonData.proto\x1a\x30POGOProtos/Data/Player/PlayerPublicProfile.proto\"\x90\x01\n\rGymMembership\x12\x32\n\x0cpokemon_data\x18\x01 \x01(\x0b\x32\x1c.POGOProtos.Data.PokemonData\x12K\n\x16trainer_public_profile\x18\x02 \x01(\x0b\x32+.POGOProtos.Data.Player.PlayerPublicProfileb\x06proto3')
  ,
  dependencies=[POGOProtos_dot_Data_dot_PokemonData__pb2.DESCRIPTOR,POGOProtos_dot_Data_dot_Player_dot_PlayerPublicProfile__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GYMMEMBERSHIP = _descriptor.Descriptor(
  name='GymMembership',
  full_name='POGOProtos.Data.Gym.GymMembership',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pokemon_data', full_name='POGOProtos.Data.Gym.GymMembership.pokemon_data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trainer_public_profile', full_name='POGOProtos.Data.Gym.GymMembership.trainer_public_profile', index=1,
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
  serialized_start=150,
  serialized_end=294,
)

_GYMMEMBERSHIP.fields_by_name['pokemon_data'].message_type = POGOProtos_dot_Data_dot_PokemonData__pb2._POKEMONDATA
_GYMMEMBERSHIP.fields_by_name['trainer_public_profile'].message_type = POGOProtos_dot_Data_dot_Player_dot_PlayerPublicProfile__pb2._PLAYERPUBLICPROFILE
DESCRIPTOR.message_types_by_name['GymMembership'] = _GYMMEMBERSHIP

GymMembership = _reflection.GeneratedProtocolMessageType('GymMembership', (_message.Message,), dict(
  DESCRIPTOR = _GYMMEMBERSHIP,
  __module__ = 'POGOProtos.Data.Gym.GymMembership_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Data.Gym.GymMembership)
  ))
_sym_db.RegisterMessage(GymMembership)


# @@protoc_insertion_point(module_scope)
