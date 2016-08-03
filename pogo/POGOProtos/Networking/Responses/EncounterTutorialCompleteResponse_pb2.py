# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Networking/Responses/EncounterTutorialCompleteResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from POGOProtos.Data import PokemonData_pb2 as POGOProtos_dot_Data_dot_PokemonData__pb2
from POGOProtos.Data.Capture import CaptureAward_pb2 as POGOProtos_dot_Data_dot_Capture_dot_CaptureAward__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos/Networking/Responses/EncounterTutorialCompleteResponse.proto',
  package='POGOProtos.Networking.Responses',
  syntax='proto3',
  serialized_pb=_b('\nGPOGOProtos/Networking/Responses/EncounterTutorialCompleteResponse.proto\x12\x1fPOGOProtos.Networking.Responses\x1a!POGOProtos/Data/PokemonData.proto\x1a*POGOProtos/Data/Capture/CaptureAward.proto\"\xad\x02\n!EncounterTutorialCompleteResponse\x12Y\n\x06result\x18\x01 \x01(\x0e\x32I.POGOProtos.Networking.Responses.EncounterTutorialCompleteResponse.Result\x12\x32\n\x0cpokemon_data\x18\x02 \x01(\x0b\x32\x1c.POGOProtos.Data.PokemonData\x12<\n\rcapture_award\x18\x03 \x01(\x0b\x32%.POGOProtos.Data.Capture.CaptureAward\";\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x19\n\x15\x45RROR_INVALID_POKEMON\x10\x02\x62\x06proto3')
  ,
  dependencies=[POGOProtos_dot_Data_dot_PokemonData__pb2.DESCRIPTOR,POGOProtos_dot_Data_dot_Capture_dot_CaptureAward__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_ENCOUNTERTUTORIALCOMPLETERESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='POGOProtos.Networking.Responses.EncounterTutorialCompleteResponse.Result',
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
      name='ERROR_INVALID_POKEMON', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=430,
  serialized_end=489,
)
_sym_db.RegisterEnumDescriptor(_ENCOUNTERTUTORIALCOMPLETERESPONSE_RESULT)


_ENCOUNTERTUTORIALCOMPLETERESPONSE = _descriptor.Descriptor(
  name='EncounterTutorialCompleteResponse',
  full_name='POGOProtos.Networking.Responses.EncounterTutorialCompleteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='POGOProtos.Networking.Responses.EncounterTutorialCompleteResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon_data', full_name='POGOProtos.Networking.Responses.EncounterTutorialCompleteResponse.pokemon_data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='capture_award', full_name='POGOProtos.Networking.Responses.EncounterTutorialCompleteResponse.capture_award', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ENCOUNTERTUTORIALCOMPLETERESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=188,
  serialized_end=489,
)

_ENCOUNTERTUTORIALCOMPLETERESPONSE.fields_by_name['result'].enum_type = _ENCOUNTERTUTORIALCOMPLETERESPONSE_RESULT
_ENCOUNTERTUTORIALCOMPLETERESPONSE.fields_by_name['pokemon_data'].message_type = POGOProtos_dot_Data_dot_PokemonData__pb2._POKEMONDATA
_ENCOUNTERTUTORIALCOMPLETERESPONSE.fields_by_name['capture_award'].message_type = POGOProtos_dot_Data_dot_Capture_dot_CaptureAward__pb2._CAPTUREAWARD
_ENCOUNTERTUTORIALCOMPLETERESPONSE_RESULT.containing_type = _ENCOUNTERTUTORIALCOMPLETERESPONSE
DESCRIPTOR.message_types_by_name['EncounterTutorialCompleteResponse'] = _ENCOUNTERTUTORIALCOMPLETERESPONSE

EncounterTutorialCompleteResponse = _reflection.GeneratedProtocolMessageType('EncounterTutorialCompleteResponse', (_message.Message,), dict(
  DESCRIPTOR = _ENCOUNTERTUTORIALCOMPLETERESPONSE,
  __module__ = 'POGOProtos.Networking.Responses.EncounterTutorialCompleteResponse_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Networking.Responses.EncounterTutorialCompleteResponse)
  ))
_sym_db.RegisterMessage(EncounterTutorialCompleteResponse)


# @@protoc_insertion_point(module_scope)
