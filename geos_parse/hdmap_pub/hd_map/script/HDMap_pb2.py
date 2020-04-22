# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: HDMap.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import Divider_pb2 as Divider__pb2
import TrafficLight_pb2 as TrafficLight__pb2
import LaneMarking_pb2 as LaneMarking__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='HDMap.proto',
  package='hdmap',
  syntax='proto3',
  serialized_pb=_b('\n\x0bHDMap.proto\x12\x05hdmap\x1a\rDivider.proto\x1a\x12TrafficLight.proto\x1a\x11LaneMarking.proto\"\xa1\x01\n\x05HDMap\x12\x10\n\x08scene_id\x18\x01 \x01(\t\x12 \n\x08\x64ividers\x18\x02 \x03(\x0b\x32\x0e.hdmap.Divider\x12)\n\x0ctafficlights\x18\x03 \x03(\x0b\x32\x13.hdmap.TrafficLight\x12(\n\x0clanemarkings\x18\x04 \x03(\x0b\x32\x12.hdmap.LaneMarking\x12\x0f\n\x07version\x18\x05 \x01(\tb\x06proto3')
  ,
  dependencies=[Divider__pb2.DESCRIPTOR,TrafficLight__pb2.DESCRIPTOR,LaneMarking__pb2.DESCRIPTOR,])




_HDMAP = _descriptor.Descriptor(
  name='HDMap',
  full_name='hdmap.HDMap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='scene_id', full_name='hdmap.HDMap.scene_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dividers', full_name='hdmap.HDMap.dividers', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tafficlights', full_name='hdmap.HDMap.tafficlights', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lanemarkings', full_name='hdmap.HDMap.lanemarkings', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='hdmap.HDMap.version', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=77,
  serialized_end=238,
)

_HDMAP.fields_by_name['dividers'].message_type = Divider__pb2._DIVIDER
_HDMAP.fields_by_name['tafficlights'].message_type = TrafficLight__pb2._TRAFFICLIGHT
_HDMAP.fields_by_name['lanemarkings'].message_type = LaneMarking__pb2._LANEMARKING
DESCRIPTOR.message_types_by_name['HDMap'] = _HDMAP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HDMap = _reflection.GeneratedProtocolMessageType('HDMap', (_message.Message,), dict(
  DESCRIPTOR = _HDMAP,
  __module__ = 'HDMap_pb2'
  # @@protoc_insertion_point(class_scope:hdmap.HDMap)
  ))
_sym_db.RegisterMessage(HDMap)


# @@protoc_insertion_point(module_scope)