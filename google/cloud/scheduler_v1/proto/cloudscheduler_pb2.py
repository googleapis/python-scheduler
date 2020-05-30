# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/scheduler_v1/proto/cloudscheduler.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.cloud.scheduler_v1.proto import (
    job_pb2 as google_dot_cloud_dot_scheduler__v1_dot_proto_dot_job__pb2,
)
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/scheduler_v1/proto/cloudscheduler.proto",
    package="google.cloud.scheduler.v1",
    syntax="proto3",
    serialized_options=b"\n\035com.google.cloud.scheduler.v1B\016SchedulerProtoP\001ZBgoogle.golang.org/genproto/googleapis/cloud/scheduler/v1;scheduler\242\002\tSCHEDULER",
    serialized_pb=b'\n4google/cloud/scheduler_v1/proto/cloudscheduler.proto\x12\x19google.cloud.scheduler.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a)google/cloud/scheduler_v1/proto/job.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"s\n\x0fListJobsRequest\x12\x39\n\x06parent\x18\x01 \x01(\tB)\xe0\x41\x02\xfa\x41#\x12!cloudscheduler.googleapis.com/Job\x12\x11\n\tpage_size\x18\x05 \x01(\x05\x12\x12\n\npage_token\x18\x06 \x01(\t"Y\n\x10ListJobsResponse\x12,\n\x04jobs\x18\x01 \x03(\x0b\x32\x1e.google.cloud.scheduler.v1.Job\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"H\n\rGetJobRequest\x12\x37\n\x04name\x18\x01 \x01(\tB)\xe0\x41\x02\xfa\x41#\n!cloudscheduler.googleapis.com/Job"\x7f\n\x10\x43reateJobRequest\x12\x39\n\x06parent\x18\x01 \x01(\tB)\xe0\x41\x02\xfa\x41#\x12!cloudscheduler.googleapis.com/Job\x12\x30\n\x03job\x18\x02 \x01(\x0b\x32\x1e.google.cloud.scheduler.v1.JobB\x03\xe0\x41\x02"z\n\x10UpdateJobRequest\x12\x30\n\x03job\x18\x01 \x01(\x0b\x32\x1e.google.cloud.scheduler.v1.JobB\x03\xe0\x41\x02\x12\x34\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x03\xe0\x41\x02"K\n\x10\x44\x65leteJobRequest\x12\x37\n\x04name\x18\x01 \x01(\tB)\xe0\x41\x02\xfa\x41#\n!cloudscheduler.googleapis.com/Job"J\n\x0fPauseJobRequest\x12\x37\n\x04name\x18\x01 \x01(\tB)\xe0\x41\x02\xfa\x41#\n!cloudscheduler.googleapis.com/Job"K\n\x10ResumeJobRequest\x12\x37\n\x04name\x18\x01 \x01(\tB)\xe0\x41\x02\xfa\x41#\n!cloudscheduler.googleapis.com/Job"H\n\rRunJobRequest\x12\x37\n\x04name\x18\x01 \x01(\tB)\xe0\x41\x02\xfa\x41#\n!cloudscheduler.googleapis.com/Job2\xb3\n\n\x0e\x43loudScheduler\x12\x9e\x01\n\x08ListJobs\x12*.google.cloud.scheduler.v1.ListJobsRequest\x1a+.google.cloud.scheduler.v1.ListJobsResponse"9\x82\xd3\xe4\x93\x02*\x12(/v1/{parent=projects/*/locations/*}/jobs\xda\x41\x06parent\x12\x8b\x01\n\x06GetJob\x12(.google.cloud.scheduler.v1.GetJobRequest\x1a\x1e.google.cloud.scheduler.v1.Job"7\x82\xd3\xe4\x93\x02*\x12(/v1/{name=projects/*/locations/*/jobs/*}\xda\x41\x04name\x12\x9c\x01\n\tCreateJob\x12+.google.cloud.scheduler.v1.CreateJobRequest\x1a\x1e.google.cloud.scheduler.v1.Job"B\x82\xd3\xe4\x93\x02/"(/v1/{parent=projects/*/locations/*}/jobs:\x03job\xda\x41\nparent,job\x12\xa5\x01\n\tUpdateJob\x12+.google.cloud.scheduler.v1.UpdateJobRequest\x1a\x1e.google.cloud.scheduler.v1.Job"K\x82\xd3\xe4\x93\x02\x33\x32,/v1/{job.name=projects/*/locations/*/jobs/*}:\x03job\xda\x41\x0fjob,update_mask\x12\x89\x01\n\tDeleteJob\x12+.google.cloud.scheduler.v1.DeleteJobRequest\x1a\x16.google.protobuf.Empty"7\x82\xd3\xe4\x93\x02**(/v1/{name=projects/*/locations/*/jobs/*}\xda\x41\x04name\x12\x98\x01\n\x08PauseJob\x12*.google.cloud.scheduler.v1.PauseJobRequest\x1a\x1e.google.cloud.scheduler.v1.Job"@\x82\xd3\xe4\x93\x02\x33"./v1/{name=projects/*/locations/*/jobs/*}:pause:\x01*\xda\x41\x04name\x12\x9b\x01\n\tResumeJob\x12+.google.cloud.scheduler.v1.ResumeJobRequest\x1a\x1e.google.cloud.scheduler.v1.Job"A\x82\xd3\xe4\x93\x02\x34"//v1/{name=projects/*/locations/*/jobs/*}:resume:\x01*\xda\x41\x04name\x12\x92\x01\n\x06RunJob\x12(.google.cloud.scheduler.v1.RunJobRequest\x1a\x1e.google.cloud.scheduler.v1.Job">\x82\xd3\xe4\x93\x02\x31",/v1/{name=projects/*/locations/*/jobs/*}:run:\x01*\xda\x41\x04name\x1aQ\xca\x41\x1d\x63loudscheduler.googleapis.com\xd2\x41.https://www.googleapis.com/auth/cloud-platformB\x81\x01\n\x1d\x63om.google.cloud.scheduler.v1B\x0eSchedulerProtoP\x01ZBgoogle.golang.org/genproto/googleapis/cloud/scheduler/v1;scheduler\xa2\x02\tSCHEDULERb\x06proto3',
    dependencies=[
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
        google_dot_api_dot_client__pb2.DESCRIPTOR,
        google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,
        google_dot_api_dot_resource__pb2.DESCRIPTOR,
        google_dot_cloud_dot_scheduler__v1_dot_proto_dot_job__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,
    ],
)


_LISTJOBSREQUEST = _descriptor.Descriptor(
    name="ListJobsRequest",
    full_name="google.cloud.scheduler.v1.ListJobsRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="parent",
            full_name="google.cloud.scheduler.v1.ListJobsRequest.parent",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\002\372A#\022!cloudscheduler.googleapis.com/Job",
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="page_size",
            full_name="google.cloud.scheduler.v1.ListJobsRequest.page_size",
            index=1,
            number=5,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="page_token",
            full_name="google.cloud.scheduler.v1.ListJobsRequest.page_token",
            index=2,
            number=6,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=304,
    serialized_end=419,
)


_LISTJOBSRESPONSE = _descriptor.Descriptor(
    name="ListJobsResponse",
    full_name="google.cloud.scheduler.v1.ListJobsResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="jobs",
            full_name="google.cloud.scheduler.v1.ListJobsResponse.jobs",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="next_page_token",
            full_name="google.cloud.scheduler.v1.ListJobsResponse.next_page_token",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=421,
    serialized_end=510,
)


_GETJOBREQUEST = _descriptor.Descriptor(
    name="GetJobRequest",
    full_name="google.cloud.scheduler.v1.GetJobRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.scheduler.v1.GetJobRequest.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\002\372A#\n!cloudscheduler.googleapis.com/Job",
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=512,
    serialized_end=584,
)


_CREATEJOBREQUEST = _descriptor.Descriptor(
    name="CreateJobRequest",
    full_name="google.cloud.scheduler.v1.CreateJobRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="parent",
            full_name="google.cloud.scheduler.v1.CreateJobRequest.parent",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\002\372A#\022!cloudscheduler.googleapis.com/Job",
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="job",
            full_name="google.cloud.scheduler.v1.CreateJobRequest.job",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\002",
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=586,
    serialized_end=713,
)


_UPDATEJOBREQUEST = _descriptor.Descriptor(
    name="UpdateJobRequest",
    full_name="google.cloud.scheduler.v1.UpdateJobRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="job",
            full_name="google.cloud.scheduler.v1.UpdateJobRequest.job",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\002",
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="update_mask",
            full_name="google.cloud.scheduler.v1.UpdateJobRequest.update_mask",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\002",
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=715,
    serialized_end=837,
)


_DELETEJOBREQUEST = _descriptor.Descriptor(
    name="DeleteJobRequest",
    full_name="google.cloud.scheduler.v1.DeleteJobRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.scheduler.v1.DeleteJobRequest.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\002\372A#\n!cloudscheduler.googleapis.com/Job",
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=839,
    serialized_end=914,
)


_PAUSEJOBREQUEST = _descriptor.Descriptor(
    name="PauseJobRequest",
    full_name="google.cloud.scheduler.v1.PauseJobRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.scheduler.v1.PauseJobRequest.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\002\372A#\n!cloudscheduler.googleapis.com/Job",
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=916,
    serialized_end=990,
)


_RESUMEJOBREQUEST = _descriptor.Descriptor(
    name="ResumeJobRequest",
    full_name="google.cloud.scheduler.v1.ResumeJobRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.scheduler.v1.ResumeJobRequest.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\002\372A#\n!cloudscheduler.googleapis.com/Job",
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=992,
    serialized_end=1067,
)


_RUNJOBREQUEST = _descriptor.Descriptor(
    name="RunJobRequest",
    full_name="google.cloud.scheduler.v1.RunJobRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.scheduler.v1.RunJobRequest.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\002\372A#\n!cloudscheduler.googleapis.com/Job",
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1069,
    serialized_end=1141,
)

_LISTJOBSRESPONSE.fields_by_name[
    "jobs"
].message_type = google_dot_cloud_dot_scheduler__v1_dot_proto_dot_job__pb2._JOB
_CREATEJOBREQUEST.fields_by_name[
    "job"
].message_type = google_dot_cloud_dot_scheduler__v1_dot_proto_dot_job__pb2._JOB
_UPDATEJOBREQUEST.fields_by_name[
    "job"
].message_type = google_dot_cloud_dot_scheduler__v1_dot_proto_dot_job__pb2._JOB
_UPDATEJOBREQUEST.fields_by_name[
    "update_mask"
].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
DESCRIPTOR.message_types_by_name["ListJobsRequest"] = _LISTJOBSREQUEST
DESCRIPTOR.message_types_by_name["ListJobsResponse"] = _LISTJOBSRESPONSE
DESCRIPTOR.message_types_by_name["GetJobRequest"] = _GETJOBREQUEST
DESCRIPTOR.message_types_by_name["CreateJobRequest"] = _CREATEJOBREQUEST
DESCRIPTOR.message_types_by_name["UpdateJobRequest"] = _UPDATEJOBREQUEST
DESCRIPTOR.message_types_by_name["DeleteJobRequest"] = _DELETEJOBREQUEST
DESCRIPTOR.message_types_by_name["PauseJobRequest"] = _PAUSEJOBREQUEST
DESCRIPTOR.message_types_by_name["ResumeJobRequest"] = _RESUMEJOBREQUEST
DESCRIPTOR.message_types_by_name["RunJobRequest"] = _RUNJOBREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListJobsRequest = _reflection.GeneratedProtocolMessageType(
    "ListJobsRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _LISTJOBSREQUEST,
        "__module__": "google.cloud.scheduler_v1.proto.cloudscheduler_pb2",
        "__doc__": """Request message for listing jobs using
  [ListJobs][google.cloud.scheduler.v1.CloudScheduler.ListJobs].
  Attributes:
      parent:
          Required. The location name. For example:
          ``projects/PROJECT_ID/locations/LOCATION_ID``.
      page_size:
          Requested page size.  The maximum page size is 500. If
          unspecified, the page size will be the maximum. Fewer jobs
          than requested might be returned, even if more jobs exist; use
          next_page_token to determine if more jobs exist.
      page_token:
          A token identifying a page of results the server will return.
          To request the first page results, page_token must be empty.
          To request the next page of results, page_token must be the
          value of [next_page_token][google.cloud.scheduler.v1.ListJobsR
          esponse.next_page_token] returned from the previous call to
          [ListJobs][google.cloud.scheduler.v1.CloudScheduler.ListJobs].
          It is an error to switch the value of
          [filter][google.cloud.scheduler.v1.ListJobsRequest.filter] or
          [order_by][google.cloud.scheduler.v1.ListJobsRequest.order_by]
          while iterating through pages.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.scheduler.v1.ListJobsRequest)
    },
)
_sym_db.RegisterMessage(ListJobsRequest)

ListJobsResponse = _reflection.GeneratedProtocolMessageType(
    "ListJobsResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _LISTJOBSRESPONSE,
        "__module__": "google.cloud.scheduler_v1.proto.cloudscheduler_pb2",
        "__doc__": """Response message for listing jobs using
  [ListJobs][google.cloud.scheduler.v1.CloudScheduler.ListJobs].
  Attributes:
      jobs:
          The list of jobs.
      next_page_token:
          A token to retrieve next page of results. Pass this value in
          the [page_token][google.cloud.scheduler.v1.ListJobsRequest.pag
          e_token] field in the subsequent call to
          [ListJobs][google.cloud.scheduler.v1.CloudScheduler.ListJobs]
          to retrieve the next page of results. If this is empty it
          indicates that there are no more results through which to
          paginate.  The page token is valid for only 2 hours.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.scheduler.v1.ListJobsResponse)
    },
)
_sym_db.RegisterMessage(ListJobsResponse)

GetJobRequest = _reflection.GeneratedProtocolMessageType(
    "GetJobRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETJOBREQUEST,
        "__module__": "google.cloud.scheduler_v1.proto.cloudscheduler_pb2",
        "__doc__": """Request message for
  [GetJob][google.cloud.scheduler.v1.CloudScheduler.GetJob].
  Attributes:
      name:
          Required. The job name. For example:
          ``projects/PROJECT_ID/locations/LOCATION_ID/jobs/JOB_ID``.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.scheduler.v1.GetJobRequest)
    },
)
_sym_db.RegisterMessage(GetJobRequest)

CreateJobRequest = _reflection.GeneratedProtocolMessageType(
    "CreateJobRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _CREATEJOBREQUEST,
        "__module__": "google.cloud.scheduler_v1.proto.cloudscheduler_pb2",
        "__doc__": """Request message for
  [CreateJob][google.cloud.scheduler.v1.CloudScheduler.CreateJob].
  Attributes:
      parent:
          Required. The location name. For example:
          ``projects/PROJECT_ID/locations/LOCATION_ID``.
      job:
          Required. The job to add. The user can optionally specify a
          name for the job in
          [name][google.cloud.scheduler.v1.Job.name].
          [name][google.cloud.scheduler.v1.Job.name] cannot be the same
          as an existing job. If a name is not specified then the system
          will generate a random unique name that will be returned
          ([name][google.cloud.scheduler.v1.Job.name]) in the response.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.scheduler.v1.CreateJobRequest)
    },
)
_sym_db.RegisterMessage(CreateJobRequest)

UpdateJobRequest = _reflection.GeneratedProtocolMessageType(
    "UpdateJobRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _UPDATEJOBREQUEST,
        "__module__": "google.cloud.scheduler_v1.proto.cloudscheduler_pb2",
        "__doc__": """Request message for
  [UpdateJob][google.cloud.scheduler.v1.CloudScheduler.UpdateJob].
  Attributes:
      job:
          Required. The new job properties.
          [name][google.cloud.scheduler.v1.Job.name] must be specified.
          Output only fields cannot be modified using UpdateJob. Any
          value specified for an output only field will be ignored.
      update_mask:
          A mask used to specify which fields of the job are being
          updated.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.scheduler.v1.UpdateJobRequest)
    },
)
_sym_db.RegisterMessage(UpdateJobRequest)

DeleteJobRequest = _reflection.GeneratedProtocolMessageType(
    "DeleteJobRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _DELETEJOBREQUEST,
        "__module__": "google.cloud.scheduler_v1.proto.cloudscheduler_pb2",
        "__doc__": """Request message for deleting a job using
  [DeleteJob][google.cloud.scheduler.v1.CloudScheduler.DeleteJob].
  Attributes:
      name:
          Required. The job name. For example:
          ``projects/PROJECT_ID/locations/LOCATION_ID/jobs/JOB_ID``.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.scheduler.v1.DeleteJobRequest)
    },
)
_sym_db.RegisterMessage(DeleteJobRequest)

PauseJobRequest = _reflection.GeneratedProtocolMessageType(
    "PauseJobRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _PAUSEJOBREQUEST,
        "__module__": "google.cloud.scheduler_v1.proto.cloudscheduler_pb2",
        "__doc__": """Request message for
  [PauseJob][google.cloud.scheduler.v1.CloudScheduler.PauseJob].
  Attributes:
      name:
          Required. The job name. For example:
          ``projects/PROJECT_ID/locations/LOCATION_ID/jobs/JOB_ID``.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.scheduler.v1.PauseJobRequest)
    },
)
_sym_db.RegisterMessage(PauseJobRequest)

ResumeJobRequest = _reflection.GeneratedProtocolMessageType(
    "ResumeJobRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _RESUMEJOBREQUEST,
        "__module__": "google.cloud.scheduler_v1.proto.cloudscheduler_pb2",
        "__doc__": """Request message for
  [ResumeJob][google.cloud.scheduler.v1.CloudScheduler.ResumeJob].
  Attributes:
      name:
          Required. The job name. For example:
          ``projects/PROJECT_ID/locations/LOCATION_ID/jobs/JOB_ID``.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.scheduler.v1.ResumeJobRequest)
    },
)
_sym_db.RegisterMessage(ResumeJobRequest)

RunJobRequest = _reflection.GeneratedProtocolMessageType(
    "RunJobRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _RUNJOBREQUEST,
        "__module__": "google.cloud.scheduler_v1.proto.cloudscheduler_pb2",
        "__doc__": """Request message for forcing a job to run now using
  [RunJob][google.cloud.scheduler.v1.CloudScheduler.RunJob].
  Attributes:
      name:
          Required. The job name. For example:
          ``projects/PROJECT_ID/locations/LOCATION_ID/jobs/JOB_ID``.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.scheduler.v1.RunJobRequest)
    },
)
_sym_db.RegisterMessage(RunJobRequest)


DESCRIPTOR._options = None
_LISTJOBSREQUEST.fields_by_name["parent"]._options = None
_GETJOBREQUEST.fields_by_name["name"]._options = None
_CREATEJOBREQUEST.fields_by_name["parent"]._options = None
_CREATEJOBREQUEST.fields_by_name["job"]._options = None
_UPDATEJOBREQUEST.fields_by_name["job"]._options = None
_UPDATEJOBREQUEST.fields_by_name["update_mask"]._options = None
_DELETEJOBREQUEST.fields_by_name["name"]._options = None
_PAUSEJOBREQUEST.fields_by_name["name"]._options = None
_RESUMEJOBREQUEST.fields_by_name["name"]._options = None
_RUNJOBREQUEST.fields_by_name["name"]._options = None

_CLOUDSCHEDULER = _descriptor.ServiceDescriptor(
    name="CloudScheduler",
    full_name="google.cloud.scheduler.v1.CloudScheduler",
    file=DESCRIPTOR,
    index=0,
    serialized_options=b"\312A\035cloudscheduler.googleapis.com\322A.https://www.googleapis.com/auth/cloud-platform",
    serialized_start=1144,
    serialized_end=2475,
    methods=[
        _descriptor.MethodDescriptor(
            name="ListJobs",
            full_name="google.cloud.scheduler.v1.CloudScheduler.ListJobs",
            index=0,
            containing_service=None,
            input_type=_LISTJOBSREQUEST,
            output_type=_LISTJOBSRESPONSE,
            serialized_options=b"\202\323\344\223\002*\022(/v1/{parent=projects/*/locations/*}/jobs\332A\006parent",
        ),
        _descriptor.MethodDescriptor(
            name="GetJob",
            full_name="google.cloud.scheduler.v1.CloudScheduler.GetJob",
            index=1,
            containing_service=None,
            input_type=_GETJOBREQUEST,
            output_type=google_dot_cloud_dot_scheduler__v1_dot_proto_dot_job__pb2._JOB,
            serialized_options=b"\202\323\344\223\002*\022(/v1/{name=projects/*/locations/*/jobs/*}\332A\004name",
        ),
        _descriptor.MethodDescriptor(
            name="CreateJob",
            full_name="google.cloud.scheduler.v1.CloudScheduler.CreateJob",
            index=2,
            containing_service=None,
            input_type=_CREATEJOBREQUEST,
            output_type=google_dot_cloud_dot_scheduler__v1_dot_proto_dot_job__pb2._JOB,
            serialized_options=b'\202\323\344\223\002/"(/v1/{parent=projects/*/locations/*}/jobs:\003job\332A\nparent,job',
        ),
        _descriptor.MethodDescriptor(
            name="UpdateJob",
            full_name="google.cloud.scheduler.v1.CloudScheduler.UpdateJob",
            index=3,
            containing_service=None,
            input_type=_UPDATEJOBREQUEST,
            output_type=google_dot_cloud_dot_scheduler__v1_dot_proto_dot_job__pb2._JOB,
            serialized_options=b"\202\323\344\223\00232,/v1/{job.name=projects/*/locations/*/jobs/*}:\003job\332A\017job,update_mask",
        ),
        _descriptor.MethodDescriptor(
            name="DeleteJob",
            full_name="google.cloud.scheduler.v1.CloudScheduler.DeleteJob",
            index=4,
            containing_service=None,
            input_type=_DELETEJOBREQUEST,
            output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
            serialized_options=b"\202\323\344\223\002**(/v1/{name=projects/*/locations/*/jobs/*}\332A\004name",
        ),
        _descriptor.MethodDescriptor(
            name="PauseJob",
            full_name="google.cloud.scheduler.v1.CloudScheduler.PauseJob",
            index=5,
            containing_service=None,
            input_type=_PAUSEJOBREQUEST,
            output_type=google_dot_cloud_dot_scheduler__v1_dot_proto_dot_job__pb2._JOB,
            serialized_options=b'\202\323\344\223\0023"./v1/{name=projects/*/locations/*/jobs/*}:pause:\001*\332A\004name',
        ),
        _descriptor.MethodDescriptor(
            name="ResumeJob",
            full_name="google.cloud.scheduler.v1.CloudScheduler.ResumeJob",
            index=6,
            containing_service=None,
            input_type=_RESUMEJOBREQUEST,
            output_type=google_dot_cloud_dot_scheduler__v1_dot_proto_dot_job__pb2._JOB,
            serialized_options=b'\202\323\344\223\0024"//v1/{name=projects/*/locations/*/jobs/*}:resume:\001*\332A\004name',
        ),
        _descriptor.MethodDescriptor(
            name="RunJob",
            full_name="google.cloud.scheduler.v1.CloudScheduler.RunJob",
            index=7,
            containing_service=None,
            input_type=_RUNJOBREQUEST,
            output_type=google_dot_cloud_dot_scheduler__v1_dot_proto_dot_job__pb2._JOB,
            serialized_options=b'\202\323\344\223\0021",/v1/{name=projects/*/locations/*/jobs/*}:run:\001*\332A\004name',
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_CLOUDSCHEDULER)

DESCRIPTOR.services_by_name["CloudScheduler"] = _CLOUDSCHEDULER

# @@protoc_insertion_point(module_scope)
