# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ngrpc.proto\"\x1d\n\rClientRequest\x12\x0c\n\x04link\x18\x01 \x01(\t\"\x1e\n\x0e\x43ommentRequest\x12\x0c\n\x04link\x18\x01 \x01(\t\",\n\x0e\x43lientResponse\x12\x1a\n\x04prod\x18\x01 \x03(\x0b\x32\x0c.ItemProduct\")\n\x0f\x43ommentResponse\x12\x16\n\x04\x63omm\x18\x01 \x03(\x0b\x32\x08.Comment\"\x83\x01\n\x0bItemProduct\x12\x0c\n\x04link\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12)\n\x0f\x63haracteristics\x18\x03 \x03(\x0b\x32\x10.Characteristics\x12\x0e\n\x06images\x18\x04 \x03(\t\x12\x0e\n\x06rating\x18\x05 \x01(\t\x12\r\n\x05price\x18\x06 \x01(\x05\".\n\x0f\x43haracteristics\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"^\n\x07\x43omment\x12\x0e\n\x06\x61vatar\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\r\n\x05grade\x18\x03 \x01(\t\x12\x14\n\x0cpublished_at\x18\x04 \x01(\t\x12\x0c\n\x04text\x18\x05 \x01(\t2<\n\x0eProductService\x12*\n\x07Product\x12\x0e.ClientRequest\x1a\x0f.ClientResponse2:\n\x0e\x43ommentService\x12(\n\x03\x43om\x12\x0f.CommentRequest\x1a\x10.CommentResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'grpc_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_CLIENTREQUEST']._serialized_start=14
  _globals['_CLIENTREQUEST']._serialized_end=43
  _globals['_COMMENTREQUEST']._serialized_start=45
  _globals['_COMMENTREQUEST']._serialized_end=75
  _globals['_CLIENTRESPONSE']._serialized_start=77
  _globals['_CLIENTRESPONSE']._serialized_end=121
  _globals['_COMMENTRESPONSE']._serialized_start=123
  _globals['_COMMENTRESPONSE']._serialized_end=164
  _globals['_ITEMPRODUCT']._serialized_start=167
  _globals['_ITEMPRODUCT']._serialized_end=298
  _globals['_CHARACTERISTICS']._serialized_start=300
  _globals['_CHARACTERISTICS']._serialized_end=346
  _globals['_COMMENT']._serialized_start=348
  _globals['_COMMENT']._serialized_end=442
  _globals['_PRODUCTSERVICE']._serialized_start=444
  _globals['_PRODUCTSERVICE']._serialized_end=504
  _globals['_COMMENTSERVICE']._serialized_start=506
  _globals['_COMMENTSERVICE']._serialized_end=564
# @@protoc_insertion_point(module_scope)