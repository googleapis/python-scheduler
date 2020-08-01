# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/scheduler_v1beta1/proto/job.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.cloud.scheduler_v1beta1.proto import target_pb2 as google_dot_cloud_dot_scheduler__v1beta1_dot_proto_dot_target__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/scheduler_v1beta1/proto/job.proto',
  package='google.cloud.scheduler.v1beta1',
  syntax='proto3',
  serialized_options=b'\n\"com.google.cloud.scheduler.v1beta1B\010JobProtoP\001ZGgoogle.golang.org/genproto/googleapis/cloud/scheduler/v1beta1;scheduler',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n.google/cloud/scheduler_v1beta1/proto/job.proto\x12\x1egoogle.cloud.scheduler.v1beta1\x1a\x19google/api/resource.proto\x1a\x31google/cloud/scheduler_v1beta1/proto/target.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto\x1a\x1cgoogle/api/annotations.proto\"\xe4\x06\n\x03Job\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x45\n\rpubsub_target\x18\x04 \x01(\x0b\x32,.google.cloud.scheduler.v1beta1.PubsubTargetH\x00\x12U\n\x16\x61pp_engine_http_target\x18\x05 \x01(\x0b\x32\x33.google.cloud.scheduler.v1beta1.AppEngineHttpTargetH\x00\x12\x41\n\x0bhttp_target\x18\x06 \x01(\x0b\x32*.google.cloud.scheduler.v1beta1.HttpTargetH\x00\x12\x10\n\x08schedule\x18\x14 \x01(\t\x12\x11\n\ttime_zone\x18\x15 \x01(\t\x12\x34\n\x10user_update_time\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x38\n\x05state\x18\n \x01(\x0e\x32).google.cloud.scheduler.v1beta1.Job.State\x12\"\n\x06status\x18\x0b \x01(\x0b\x32\x12.google.rpc.Status\x12\x31\n\rschedule_time\x18\x11 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x35\n\x11last_attempt_time\x18\x12 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x41\n\x0cretry_config\x18\x13 \x01(\x0b\x32+.google.cloud.scheduler.v1beta1.RetryConfig\x12\x33\n\x10\x61ttempt_deadline\x18\x16 \x01(\x0b\x32\x19.google.protobuf.Duration\"X\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07\x45NABLED\x10\x01\x12\n\n\x06PAUSED\x10\x02\x12\x0c\n\x08\x44ISABLED\x10\x03\x12\x11\n\rUPDATE_FAILED\x10\x04:Z\xea\x41W\n!cloudscheduler.googleapis.com/Job\x12\x32projects/{project}/locations/{location}/jobs/{job}B\x08\n\x06target\"\xe2\x01\n\x0bRetryConfig\x12\x13\n\x0bretry_count\x18\x01 \x01(\x05\x12\x35\n\x12max_retry_duration\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x37\n\x14min_backoff_duration\x18\x03 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x37\n\x14max_backoff_duration\x18\x04 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x15\n\rmax_doublings\x18\x05 \x01(\x05\x42y\n\"com.google.cloud.scheduler.v1beta1B\x08JobProtoP\x01ZGgoogle.golang.org/genproto/googleapis/cloud/scheduler/v1beta1;schedulerb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_cloud_dot_scheduler__v1beta1_dot_proto_dot_target__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_JOB_STATE = _descriptor.EnumDescriptor(
  name='State',
  full_name='google.cloud.scheduler.v1beta1.Job.State',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ENABLED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PAUSED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DISABLED', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UPDATE_FAILED', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=959,
  serialized_end=1047,
)
_sym_db.RegisterEnumDescriptor(_JOB_STATE)


_JOB = _descriptor.Descriptor(
  name='Job',
  full_name='google.cloud.scheduler.v1beta1.Job',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.scheduler.v1beta1.Job.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='google.cloud.scheduler.v1beta1.Job.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pubsub_target', full_name='google.cloud.scheduler.v1beta1.Job.pubsub_target', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='app_engine_http_target', full_name='google.cloud.scheduler.v1beta1.Job.app_engine_http_target', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='http_target', full_name='google.cloud.scheduler.v1beta1.Job.http_target', index=4,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='schedule', full_name='google.cloud.scheduler.v1beta1.Job.schedule', index=5,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time_zone', full_name='google.cloud.scheduler.v1beta1.Job.time_zone', index=6,
      number=21, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_update_time', full_name='google.cloud.scheduler.v1beta1.Job.user_update_time', index=7,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='google.cloud.scheduler.v1beta1.Job.state', index=8,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='google.cloud.scheduler.v1beta1.Job.status', index=9,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='schedule_time', full_name='google.cloud.scheduler.v1beta1.Job.schedule_time', index=10,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_attempt_time', full_name='google.cloud.scheduler.v1beta1.Job.last_attempt_time', index=11,
      number=18, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='retry_config', full_name='google.cloud.scheduler.v1beta1.Job.retry_config', index=12,
      number=19, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='attempt_deadline', full_name='google.cloud.scheduler.v1beta1.Job.attempt_deadline', index=13,
      number=22, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _JOB_STATE,
  ],
  serialized_options=b'\352AW\n!cloudscheduler.googleapis.com/Job\0222projects/{project}/locations/{location}/jobs/{job}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='target', full_name='google.cloud.scheduler.v1beta1.Job.target',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=281,
  serialized_end=1149,
)


_RETRYCONFIG = _descriptor.Descriptor(
  name='RetryConfig',
  full_name='google.cloud.scheduler.v1beta1.RetryConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='retry_count', full_name='google.cloud.scheduler.v1beta1.RetryConfig.retry_count', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_retry_duration', full_name='google.cloud.scheduler.v1beta1.RetryConfig.max_retry_duration', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='min_backoff_duration', full_name='google.cloud.scheduler.v1beta1.RetryConfig.min_backoff_duration', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_backoff_duration', full_name='google.cloud.scheduler.v1beta1.RetryConfig.max_backoff_duration', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_doublings', full_name='google.cloud.scheduler.v1beta1.RetryConfig.max_doublings', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1152,
  serialized_end=1378,
)

_JOB.fields_by_name['pubsub_target'].message_type = google_dot_cloud_dot_scheduler__v1beta1_dot_proto_dot_target__pb2._PUBSUBTARGET
_JOB.fields_by_name['app_engine_http_target'].message_type = google_dot_cloud_dot_scheduler__v1beta1_dot_proto_dot_target__pb2._APPENGINEHTTPTARGET
_JOB.fields_by_name['http_target'].message_type = google_dot_cloud_dot_scheduler__v1beta1_dot_proto_dot_target__pb2._HTTPTARGET
_JOB.fields_by_name['user_update_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_JOB.fields_by_name['state'].enum_type = _JOB_STATE
_JOB.fields_by_name['status'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_JOB.fields_by_name['schedule_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_JOB.fields_by_name['last_attempt_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_JOB.fields_by_name['retry_config'].message_type = _RETRYCONFIG
_JOB.fields_by_name['attempt_deadline'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_JOB_STATE.containing_type = _JOB
_JOB.oneofs_by_name['target'].fields.append(
  _JOB.fields_by_name['pubsub_target'])
_JOB.fields_by_name['pubsub_target'].containing_oneof = _JOB.oneofs_by_name['target']
_JOB.oneofs_by_name['target'].fields.append(
  _JOB.fields_by_name['app_engine_http_target'])
_JOB.fields_by_name['app_engine_http_target'].containing_oneof = _JOB.oneofs_by_name['target']
_JOB.oneofs_by_name['target'].fields.append(
  _JOB.fields_by_name['http_target'])
_JOB.fields_by_name['http_target'].containing_oneof = _JOB.oneofs_by_name['target']
_RETRYCONFIG.fields_by_name['max_retry_duration'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_RETRYCONFIG.fields_by_name['min_backoff_duration'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_RETRYCONFIG.fields_by_name['max_backoff_duration'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
DESCRIPTOR.message_types_by_name['Job'] = _JOB
DESCRIPTOR.message_types_by_name['RetryConfig'] = _RETRYCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Job = _reflection.GeneratedProtocolMessageType('Job', (_message.Message,), {
  'DESCRIPTOR' : _JOB,
  '__module__' : 'google.cloud.scheduler_v1beta1.proto.job_pb2'
  ,
  '__doc__': """Configuration for a job. The maximum allowed size for a job is 100KB.
  
  Attributes:
      name:
          Optionally caller-specified in [CreateJob][google.cloud.schedu
          ler.v1beta1.CloudScheduler.CreateJob], after which it becomes
          output only.  The job name. For example:
          ``projects/PROJECT_ID/locations/LOCATION_ID/jobs/JOB_ID``.  -
          ``PROJECT_ID`` can contain letters ([A-Za-z]), numbers
          ([0-9]),    hyphens (-), colons (:), or periods (.). For more
          information, see    `Identifying    projects
          <https://cloud.google.com/resource-manager/docs/creating-
          managing-projects#identifying_projects>`__ -  ``LOCATION_ID``
          is the canonical ID for the job’s location. The list    of
          available locations can be obtained by calling    [ListLocatio
          ns][google.cloud.location.Locations.ListLocations]. For
          more information, see
          https://cloud.google.com/about/locations/. -  ``JOB_ID`` can
          contain only letters ([A-Za-z]), numbers ([0-9]),    hyphens
          (-), or underscores (_). The maximum length is 500
          characters.
      description:
          Optionally caller-specified in [CreateJob][google.cloud.schedu
          ler.v1beta1.CloudScheduler.CreateJob] or [UpdateJob][google.cl
          oud.scheduler.v1beta1.CloudScheduler.UpdateJob].  A human-
          readable description for the job. This string must not contain
          more than 500 characters.
      target:
          Required.  Delivery settings containing destination and
          parameters.
      pubsub_target:
          Pub/Sub target.
      app_engine_http_target:
          App Engine HTTP target.
      http_target:
          HTTP target.
      schedule:
          Required, except when used with [UpdateJob][google.cloud.sched
          uler.v1beta1.CloudScheduler.UpdateJob].  Describes the
          schedule on which the job will be executed.  The schedule can
          be either of the following types:  -  `Crontab
          <http://en.wikipedia.org/wiki/Cron#Overview>`__ -  English-
          like    `schedule
          <https://cloud.google.com/scheduler/docs/configuring/cron-job-
          schedules>`__  As a general rule, execution ``n + 1`` of a job
          will not begin until execution ``n`` has finished. Cloud
          Scheduler will never allow two simultaneously outstanding
          executions. For example, this implies that if the ``n+1``\ th
          execution is scheduled to run at 16:00 but the ``n``\ th
          execution takes until 16:15, the ``n+1``\ th execution will
          not start until ``16:15``. A scheduled start time will be
          delayed if the previous execution has not ended when its
          scheduled time occurs.  If [retry_count][google.cloud.schedule
          r.v1beta1.RetryConfig.retry_count] > 0 and a job attempt
          fails, the job will be tried a total of [retry_count][google.c
          loud.scheduler.v1beta1.RetryConfig.retry_count] times, with
          exponential backoff, until the next scheduled start time.
      time_zone:
          Specifies the time zone to be used in interpreting
          [schedule][google.cloud.scheduler.v1beta1.Job.schedule]. The
          value of this field must be a time zone name from the `tz
          database <http://en.wikipedia.org/wiki/Tz_database>`__.  Note
          that some time zones include a provision for daylight savings
          time. The rules for daylight saving time are determined by the
          chosen tz. For UTC use the string “utc”. If a time zone is not
          specified, the default will be in UTC (also known as GMT).
      user_update_time:
          Output only. The creation time of the job.
      state:
          Output only. State of the job.
      status:
          Output only. The response from the target for the last
          attempted execution.
      schedule_time:
          Output only. The next time the job is scheduled. Note that
          this may be a retry of a previously failed attempt or the next
          execution time according to the schedule.
      last_attempt_time:
          Output only. The time the last job attempt started.
      retry_config:
          Settings that determine the retry behavior.
      attempt_deadline:
          The deadline for job attempts. If the request handler does not
          respond by this deadline then the request is cancelled and the
          attempt is marked as a ``DEADLINE_EXCEEDED`` failure. The
          failed attempt can be viewed in execution logs. Cloud
          Scheduler will retry the job according to the
          [RetryConfig][google.cloud.scheduler.v1beta1.RetryConfig].
          The allowed duration for this deadline is:  -  For [HTTP
          targets][google.cloud.scheduler.v1beta1.Job.http_target],
          between 15 seconds and 30 minutes. -  For [App Engine HTTP    
          targets][google.cloud.scheduler.v1beta1.Job.app_engine_http_ta
          rget],    between 15 seconds and 24 hours. -  For [PubSub
          targets][google.cloud.scheduler.v1beta1.Job.pubsub_target],
          this    field is ignored.
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.scheduler.v1beta1.Job)
  })
_sym_db.RegisterMessage(Job)

RetryConfig = _reflection.GeneratedProtocolMessageType('RetryConfig', (_message.Message,), {
  'DESCRIPTOR' : _RETRYCONFIG,
  '__module__' : 'google.cloud.scheduler_v1beta1.proto.job_pb2'
  ,
  '__doc__': """Settings that determine the retry behavior.  By default, if a job does
  not complete successfully (meaning that an acknowledgement is not
  received from the handler, then it will be retried with exponential
  backoff according to the settings in
  [RetryConfig][google.cloud.scheduler.v1beta1.RetryConfig].
  
  Attributes:
      retry_count:
          The number of attempts that the system will make to run a job
          using the exponential backoff procedure described by [max_doub
          lings][google.cloud.scheduler.v1beta1.RetryConfig.max_doubling
          s].  The default value of retry_count is zero.  If retry_count
          is zero, a job attempt will *not* be retried if it fails.
          Instead the Cloud Scheduler system will wait for the next
          scheduled execution time.  If retry_count is set to a non-zero
          number then Cloud Scheduler will retry failed attempts, using
          exponential backoff, retry_count times, or until the next
          scheduled execution time, whichever comes first.  Values
          greater than 5 and negative values are not allowed.
      max_retry_duration:
          The time limit for retrying a failed job, measured from time
          when an execution was first attempted. If specified with [retr
          y_count][google.cloud.scheduler.v1beta1.RetryConfig.retry_coun
          t], the job will be retried until both limits are reached.
          The default value for max_retry_duration is zero, which means
          retry duration is unlimited.
      min_backoff_duration:
          The minimum amount of time to wait before retrying a job after
          it fails.  The default value of this field is 5 seconds.
      max_backoff_duration:
          The maximum amount of time to wait before retrying a job after
          it fails.  The default value of this field is 1 hour.
      max_doublings:
          The time between retries will double ``max_doublings`` times.
          A job’s retry interval starts at [min_backoff_duration][google
          .cloud.scheduler.v1beta1.RetryConfig.min_backoff_duration],
          then doubles ``max_doublings`` times, then increases linearly,
          and finally retries retries at intervals of [max_backoff_durat
          ion][google.cloud.scheduler.v1beta1.RetryConfig.max_backoff_du
          ration] up to [retry_count][google.cloud.scheduler.v1beta1.Ret
          ryConfig.retry_count] times.  For example, if [min_backoff_dur
          ation][google.cloud.scheduler.v1beta1.RetryConfig.min_backoff_
          duration] is 10s, [max_backoff_duration][google.cloud.schedule
          r.v1beta1.RetryConfig.max_backoff_duration] is 300s, and
          ``max_doublings`` is 3, then the a job will first be retried
          in 10s. The retry interval will double three times, and then
          increase linearly by 2^3 \* 10s. Finally, the job will retry
          at intervals of [max_backoff_duration][google.cloud.scheduler.
          v1beta1.RetryConfig.max_backoff_duration] until the job has
          been attempted [retry_count][google.cloud.scheduler.v1beta1.Re
          tryConfig.retry_count] times. Thus, the requests will retry at
          10s, 20s, 40s, 80s, 160s, 240s, 300s, 300s, ….  The default
          value of this field is 5.
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.scheduler.v1beta1.RetryConfig)
  })
_sym_db.RegisterMessage(RetryConfig)


DESCRIPTOR._options = None
_JOB._options = None
# @@protoc_insertion_point(module_scope)
