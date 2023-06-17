# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cctv_crud.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x63\x63tv_crud.proto\x12\x08\x63\x63tvCrud\x1a\x1fgoogle/protobuf/timestamp.proto\"-\n\x1aGetApplicationByUidRequest\x12\x0f\n\x07\x61pp_uid\x18\x01 \x01(\t\"Z\n\x13\x41pplicationResponse\x12\x32\n\x0b\x61pplication\x18\x01 \x01(\x0b\x32\x1d.cctvCrud.ApplicationFullData\x12\x0f\n\x07success\x18\x02 \x01(\x08\"\xe9\x01\n\x13\x41pplicationFullData\x12\x0f\n\x07\x61pp_uid\x18\x01 \x01(\t\x12\x10\n\x08group_id\x18\x02 \x01(\t\x12\x0c\n\x04host\x18\x03 \x01(\t\x12.\n\ncreated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\nis_enabled\x18\x06 \x01(\x08\x12\x18\n\x10\x61pplication_info\x18\x07 \x01(\t\x12\x13\n\x0b\x61pp_type_id\x18\x08 \x01(\x05\"\xee\x01\n\x18\x43reateApplicationRequest\x12\x0f\n\x07\x61pp_uid\x18\x01 \x01(\t\x12\x10\n\x08group_id\x18\x02 \x01(\t\x12\x0c\n\x04host\x18\x03 \x01(\t\x12.\n\ncreated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\nis_enabled\x18\x06 \x01(\x08\x12\x18\n\x10\x61pplication_info\x18\x07 \x01(\t\x12\x13\n\x0b\x61pp_type_id\x18\x08 \x01(\x05\"E\n\x12\x41pplicationRequest\x12\x0f\n\x07\x61pp_uid\x18\x01 \x01(\t\x12\x10\n\x08group_id\x18\x02 \x01(\t\x12\x0c\n\x04host\x18\x03 \x01(\t\",\n\x1cListApplicationByHostRequest\x12\x0c\n\x04host\x18\x01 \x01(\t\"_\n\x17ListApplicationResponse\x12\x33\n\x0c\x61pplications\x18\x01 \x03(\x0b\x32\x1d.cctvCrud.ApplicationFullData\x12\x0f\n\x07success\x18\x02 \x01(\x08\"+\n\x15GetCameraByUidRequest\x12\x12\n\ncamera_uid\x18\x01 \x01(\t\"\xe9\x01\n\x13\x43reateCameraRequest\x12\x12\n\ncamera_uid\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\nis_enabled\x18\x05 \x01(\x08\x12\x13\n\x0b\x63\x61mera_info\x18\x06 \x01(\t\x12\x15\n\rraw_input_url\x18\x07 \x01(\t\x12\x10\n\x08group_id\x18\x08 \x01(\t\"\xd2\x01\n\x0e\x43\x61meraFullData\x12\x12\n\ncamera_uid\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\nis_enabled\x18\x05 \x01(\x08\x12\x13\n\x0b\x63\x61mera_info\x18\x06 \x01(\t\x12\x15\n\rraw_input_url\x18\x07 \x01(\t\"K\n\x0e\x43\x61meraResponse\x12(\n\x06\x63\x61mera\x18\x01 \x01(\x0b\x32\x18.cctvCrud.CameraFullData\x12\x0f\n\x07success\x18\x02 \x01(\x08\"C\n\rCameraRequest\x12\x12\n\ncamera_uid\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08group_id\x18\x03 \x01(\t\"_\n\x0e\x41ppTypeRequest\x12\x13\n\x0b\x61pp_type_id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x15\n\rapp_type_info\x18\x04 \x01(\t\"\'\n\x17GetAppTypeByNameRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\",\n\x15GetAppTypeByIdRequest\x12\x13\n\x0b\x61pp_type_id\x18\x01 \x01(\x05\"O\n\x0f\x41ppTypeResponse\x12+\n\x08\x61pp_type\x18\x01 \x01(\x0b\x32\x19.cctvCrud.AppTypeFullData\x12\x0f\n\x07success\x18\x02 \x01(\x08\"\xd4\x01\n\x0f\x41ppTypeFullData\x12\x13\n\x0b\x61pp_type_id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12.\n\ncreated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\nis_enabled\x18\x06 \x01(\x08\x12\x15\n\rapp_type_info\x18\x07 \x01(\t\"\xc4\x01\n\x14\x43reateAppTypeRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\nis_enabled\x18\x05 \x01(\x08\x12\x15\n\rapp_type_info\x18\x06 \x01(\t\"9\n#ListMediaChannelsByCameraUidRequest\x12\x12\n\ncamera_uid\x18\x01 \x01(\t\"`\n\x15MediaChannelsResponse\x12\x36\n\x0emedia_channels\x18\x01 \x01(\x0b\x32\x1e.cctvCrud.MediaChannelsRequest\x12\x0f\n\x07success\x18\x02 \x01(\x08\"\xfb\x01\n\x14MediaChannelsRequest\x12\x18\n\x10media_channel_id\x18\x01 \x01(\x05\x12\x12\n\ncamera_uid\x18\x02 \x01(\t\x12\x0f\n\x07\x61pp_uid\x18\x03 \x01(\t\x12\x1a\n\x12media_channel_info\x18\x04 \x01(\t\x12\x12\n\nis_enabled\x18\x05 \x01(\x08\x12.\n\ncreated_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x14\n\x0cis_recording\x18\x08 \x01(\x08\"d\n\x19ListMediaChannelsResponse\x12\x36\n\x0emedia_channels\x18\x01 \x03(\x0b\x32\x1e.cctvCrud.MediaChannelsRequest\x12\x0f\n\x07success\x18\x02 \x01(\x08\x32\xfb\x0c\n\x08\x43\x63tvCrud\x12J\n\x15UpdateCameraNameByUid\x12\x17.cctvCrud.CameraRequest\x1a\x18.cctvCrud.CameraResponse\x12K\n\x0eGetCameraByUid\x12\x1f.cctvCrud.GetCameraByUidRequest\x1a\x18.cctvCrud.CameraFullData\x12G\n\x0c\x43reateCamera\x12\x1d.cctvCrud.CreateCameraRequest\x1a\x18.cctvCrud.CameraResponse\x12\x46\n\x11\x44\x65leteCameraByUid\x12\x17.cctvCrud.CameraRequest\x1a\x18.cctvCrud.CameraResponse\x12Y\n\x1aUpdateApplicationHostByUid\x12\x1c.cctvCrud.ApplicationRequest\x1a\x1d.cctvCrud.ApplicationResponse\x12Z\n\x13GetApplicationByUid\x12$.cctvCrud.GetApplicationByUidRequest\x1a\x1d.cctvCrud.ApplicationFullData\x12\x62\n\x15ListApplicationByHost\x12&.cctvCrud.ListApplicationByHostRequest\x1a!.cctvCrud.ListApplicationResponse\x12V\n\x11\x43reateApplication\x12\".cctvCrud.CreateApplicationRequest\x1a\x1d.cctvCrud.ApplicationResponse\x12U\n\x16\x44\x65leteApplicationByUid\x12\x1c.cctvCrud.ApplicationRequest\x1a\x1d.cctvCrud.ApplicationResponse\x12H\n\x11UpdateAppTypeById\x12\x18.cctvCrud.AppTypeRequest\x1a\x19.cctvCrud.AppTypeResponse\x12P\n\x10GetAppTypeByName\x12!.cctvCrud.GetAppTypeByNameRequest\x1a\x19.cctvCrud.AppTypeFullData\x12L\n\x0eGetAppTypeById\x12\x1f.cctvCrud.GetAppTypeByIdRequest\x1a\x19.cctvCrud.AppTypeFullData\x12J\n\rCreateAppType\x12\x1e.cctvCrud.CreateAppTypeRequest\x1a\x19.cctvCrud.AppTypeResponse\x12H\n\x11\x44\x65leteAppTypeById\x12\x18.cctvCrud.AppTypeRequest\x1a\x19.cctvCrud.AppTypeResponse\x12\x66\n#UpdateMediaChannelsByMediaChannelId\x12\x1e.cctvCrud.MediaChannelsRequest\x1a\x1f.cctvCrud.MediaChannelsResponse\x12r\n\x1cListMediaChannelsByCameraUid\x12-.cctvCrud.ListMediaChannelsByCameraUidRequest\x1a#.cctvCrud.ListMediaChannelsResponse\x12`\n\x19ListMediaChannelsByAppUid\x12\x1e.cctvCrud.MediaChannelsRequest\x1a#.cctvCrud.ListMediaChannelsResponse\x12V\n\x13\x43reateMediaChannels\x12\x1e.cctvCrud.MediaChannelsRequest\x1a\x1f.cctvCrud.MediaChannelsResponse\x12\x65\n\x1e\x44\x65leteMediaChannelsByCameraUid\x12\x1e.cctvCrud.MediaChannelsRequest\x1a#.cctvCrud.ListMediaChannelsResponseB\x14Z\x12./pkg/api/cctvCrudb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cctv_crud_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\022./pkg/api/cctvCrud'
  _GETAPPLICATIONBYUIDREQUEST._serialized_start=62
  _GETAPPLICATIONBYUIDREQUEST._serialized_end=107
  _APPLICATIONRESPONSE._serialized_start=109
  _APPLICATIONRESPONSE._serialized_end=199
  _APPLICATIONFULLDATA._serialized_start=202
  _APPLICATIONFULLDATA._serialized_end=435
  _CREATEAPPLICATIONREQUEST._serialized_start=438
  _CREATEAPPLICATIONREQUEST._serialized_end=676
  _APPLICATIONREQUEST._serialized_start=678
  _APPLICATIONREQUEST._serialized_end=747
  _LISTAPPLICATIONBYHOSTREQUEST._serialized_start=749
  _LISTAPPLICATIONBYHOSTREQUEST._serialized_end=793
  _LISTAPPLICATIONRESPONSE._serialized_start=795
  _LISTAPPLICATIONRESPONSE._serialized_end=890
  _GETCAMERABYUIDREQUEST._serialized_start=892
  _GETCAMERABYUIDREQUEST._serialized_end=935
  _CREATECAMERAREQUEST._serialized_start=938
  _CREATECAMERAREQUEST._serialized_end=1171
  _CAMERAFULLDATA._serialized_start=1174
  _CAMERAFULLDATA._serialized_end=1384
  _CAMERARESPONSE._serialized_start=1386
  _CAMERARESPONSE._serialized_end=1461
  _CAMERAREQUEST._serialized_start=1463
  _CAMERAREQUEST._serialized_end=1530
  _APPTYPEREQUEST._serialized_start=1532
  _APPTYPEREQUEST._serialized_end=1627
  _GETAPPTYPEBYNAMEREQUEST._serialized_start=1629
  _GETAPPTYPEBYNAMEREQUEST._serialized_end=1668
  _GETAPPTYPEBYIDREQUEST._serialized_start=1670
  _GETAPPTYPEBYIDREQUEST._serialized_end=1714
  _APPTYPERESPONSE._serialized_start=1716
  _APPTYPERESPONSE._serialized_end=1795
  _APPTYPEFULLDATA._serialized_start=1798
  _APPTYPEFULLDATA._serialized_end=2010
  _CREATEAPPTYPEREQUEST._serialized_start=2013
  _CREATEAPPTYPEREQUEST._serialized_end=2209
  _LISTMEDIACHANNELSBYCAMERAUIDREQUEST._serialized_start=2211
  _LISTMEDIACHANNELSBYCAMERAUIDREQUEST._serialized_end=2268
  _MEDIACHANNELSRESPONSE._serialized_start=2270
  _MEDIACHANNELSRESPONSE._serialized_end=2366
  _MEDIACHANNELSREQUEST._serialized_start=2369
  _MEDIACHANNELSREQUEST._serialized_end=2620
  _LISTMEDIACHANNELSRESPONSE._serialized_start=2622
  _LISTMEDIACHANNELSRESPONSE._serialized_end=2722
  _CCTVCRUD._serialized_start=2725
  _CCTVCRUD._serialized_end=4384
# @@protoc_insertion_point(module_scope)
