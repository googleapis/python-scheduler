# -*- coding: utf-8 -*-
#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Accesses the google.cloud.scheduler.v1beta1 CloudScheduler API."""

import functools
import pkg_resources
import warnings

from google.oauth2 import service_account
import google.api_core.client_options
import google.api_core.gapic_v1.client_info
import google.api_core.gapic_v1.config
import google.api_core.gapic_v1.method
import google.api_core.gapic_v1.routing_header
import google.api_core.grpc_helpers
import google.api_core.page_iterator
import google.api_core.path_template
import grpc

from google.cloud.scheduler_v1beta1.gapic import cloud_scheduler_client_config
from google.cloud.scheduler_v1beta1.gapic import enums
from google.cloud.scheduler_v1beta1.gapic.transports import (
    cloud_scheduler_grpc_transport,
)
from google.cloud.scheduler_v1beta1.proto import cloudscheduler_pb2
from google.cloud.scheduler_v1beta1.proto import cloudscheduler_pb2_grpc
from google.cloud.scheduler_v1beta1.proto import job_pb2
from google.protobuf import empty_pb2
from google.protobuf import field_mask_pb2


_GAPIC_LIBRARY_VERSION = pkg_resources.get_distribution(
    "google-cloud-scheduler"
).version


class CloudSchedulerClient(object):
    """
    The Cloud Scheduler API allows external entities to reliably
    schedule asynchronous jobs.
    """

    SERVICE_ADDRESS = "cloudscheduler.googleapis.com:443"
    """The default address of the service."""

    # The name of the interface for this client. This is the key used to
    # find the method configuration in the client_config dictionary.
    _INTERFACE_NAME = "google.cloud.scheduler.v1beta1.CloudScheduler"

    @classmethod
    def from_service_account_file(cls, filename, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
        file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            CloudSchedulerClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @classmethod
    def job_path(cls, project, location, job):
        """Return a fully-qualified job string."""
        return google.api_core.path_template.expand(
            "projects/{project}/locations/{location}/jobs/{job}",
            project=project,
            location=location,
            job=job,
        )

    @classmethod
    def location_path(cls, project, location):
        """Return a fully-qualified location string."""
        return google.api_core.path_template.expand(
            "projects/{project}/locations/{location}",
            project=project,
            location=location,
        )

    def __init__(
        self,
        transport=None,
        channel=None,
        credentials=None,
        client_config=None,
        client_info=None,
        client_options=None,
    ):
        """Constructor.

        Args:
            transport (Union[~.CloudSchedulerGrpcTransport,
                    Callable[[~.Credentials, type], ~.CloudSchedulerGrpcTransport]): A transport
                instance, responsible for actually making the API calls.
                The default transport uses the gRPC protocol.
                This argument may also be a callable which returns a
                transport instance. Callables will be sent the credentials
                as the first argument and the default transport class as
                the second argument.
            channel (grpc.Channel): DEPRECATED. A ``Channel`` instance
                through which to make calls. This argument is mutually exclusive
                with ``credentials``; providing both will raise an exception.
            credentials (google.auth.credentials.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is mutually exclusive with providing a
                transport instance to ``transport``; doing so will raise
                an exception.
            client_config (dict): DEPRECATED. A dictionary of call options for
                each method. If not specified, the default configuration is used.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            client_options (Union[dict, google.api_core.client_options.ClientOptions]):
                Client options used to set user options on the client. API Endpoint
                should be set through client_options.
        """
        # Raise deprecation warnings for things we want to go away.
        if client_config is not None:
            warnings.warn(
                "The `client_config` argument is deprecated.",
                PendingDeprecationWarning,
                stacklevel=2,
            )
        else:
            client_config = cloud_scheduler_client_config.config

        if channel:
            warnings.warn(
                "The `channel` argument is deprecated; use " "`transport` instead.",
                PendingDeprecationWarning,
                stacklevel=2,
            )

        api_endpoint = self.SERVICE_ADDRESS
        if client_options:
            if type(client_options) == dict:
                client_options = google.api_core.client_options.from_dict(
                    client_options
                )
            if client_options.api_endpoint:
                api_endpoint = client_options.api_endpoint

        # Instantiate the transport.
        # The transport is responsible for handling serialization and
        # deserialization and actually sending data to the service.
        if transport:
            if callable(transport):
                self.transport = transport(
                    credentials=credentials,
                    default_class=cloud_scheduler_grpc_transport.CloudSchedulerGrpcTransport,
                    address=api_endpoint,
                )
            else:
                if credentials:
                    raise ValueError(
                        "Received both a transport instance and "
                        "credentials; these are mutually exclusive."
                    )
                self.transport = transport
        else:
            self.transport = cloud_scheduler_grpc_transport.CloudSchedulerGrpcTransport(
                address=api_endpoint, channel=channel, credentials=credentials
            )

        if client_info is None:
            client_info = google.api_core.gapic_v1.client_info.ClientInfo(
                gapic_version=_GAPIC_LIBRARY_VERSION
            )
        else:
            client_info.gapic_version = _GAPIC_LIBRARY_VERSION
        self._client_info = client_info

        # Parse out the default settings for retry and timeout for each RPC
        # from the client configuration.
        # (Ordinarily, these are the defaults specified in the `*_config.py`
        # file next to this one.)
        self._method_configs = google.api_core.gapic_v1.config.parse_method_configs(
            client_config["interfaces"][self._INTERFACE_NAME]
        )

        # Save a dictionary of cached API call functions.
        # These are the actual callables which invoke the proper
        # transport methods, wrapped with `wrap_method` to add retry,
        # timeout, and the like.
        self._inner_api_calls = {}

    # Service calls
    def list_jobs(
        self,
        parent,
        page_size=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Lists jobs.

        Example:
            >>> from google.cloud import scheduler_v1beta1
            >>>
            >>> client = scheduler_v1beta1.CloudSchedulerClient()
            >>>
            >>> parent = client.location_path('[PROJECT]', '[LOCATION]')
            >>>
            >>> # Iterate over all results
            >>> for element in client.list_jobs(parent):
            ...     # process element
            ...     pass
            >>>
            >>>
            >>> # Alternatively:
            >>>
            >>> # Iterate over results one page at a time
            >>> for page in client.list_jobs(parent).pages:
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            parent (str): Request message for deleting a job using ``DeleteJob``.
            page_size (int): The maximum number of resources contained in the
                underlying API response. If page streaming is performed per-
                resource, this parameter does not affect the return value. If page
                streaming is performed per-page, this determines the maximum number
                of resources in a page.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.api_core.page_iterator.PageIterator` instance.
            An iterable of :class:`~google.cloud.scheduler_v1beta1.types.Job` instances.
            You can also iterate over the pages of the response
            using its `pages` property.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "list_jobs" not in self._inner_api_calls:
            self._inner_api_calls[
                "list_jobs"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_jobs,
                default_retry=self._method_configs["ListJobs"].retry,
                default_timeout=self._method_configs["ListJobs"].timeout,
                client_info=self._client_info,
            )

        request = cloudscheduler_pb2.ListJobsRequest(parent=parent, page_size=page_size)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        iterator = google.api_core.page_iterator.GRPCIterator(
            client=None,
            method=functools.partial(
                self._inner_api_calls["list_jobs"],
                retry=retry,
                timeout=timeout,
                metadata=metadata,
            ),
            request=request,
            items_field="jobs",
            request_token_field="page_token",
            response_token_field="next_page_token",
        )
        return iterator

    def get_job(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Gets a job.

        Example:
            >>> from google.cloud import scheduler_v1beta1
            >>>
            >>> client = scheduler_v1beta1.CloudSchedulerClient()
            >>>
            >>> name = client.job_path('[PROJECT]', '[LOCATION]', '[JOB]')
            >>>
            >>> response = client.get_job(name)

        Args:
            name (str): The resource has one pattern, but the API owner expects to add more
                later. (This is the inverse of ORIGINALLY_SINGLE_PATTERN, and prevents
                that from being necessary once there are multiple patterns.)
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.scheduler_v1beta1.types.Job` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "get_job" not in self._inner_api_calls:
            self._inner_api_calls[
                "get_job"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_job,
                default_retry=self._method_configs["GetJob"].retry,
                default_timeout=self._method_configs["GetJob"].timeout,
                client_info=self._client_info,
            )

        request = cloudscheduler_pb2.GetJobRequest(name=name)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["get_job"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def create_job(
        self,
        parent,
        job,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Creates a job.

        Example:
            >>> from google.cloud import scheduler_v1beta1
            >>>
            >>> client = scheduler_v1beta1.CloudSchedulerClient()
            >>>
            >>> parent = client.location_path('[PROJECT]', '[LOCATION]')
            >>>
            >>> # TODO: Initialize `job`:
            >>> job = {}
            >>>
            >>> response = client.create_job(parent, job)

        Args:
            parent (str): Each of the definitions above may have "options" attached. These are
                just annotations which may cause code to be generated slightly
                differently or may contain hints for code that manipulates protocol
                messages.

                Clients may define custom options as extensions of the \*Options
                messages. These extensions may not yet be known at parsing time, so the
                parser cannot store the values in them. Instead it stores them in a
                field in the \*Options message called uninterpreted_option. This field
                must have the same name across all \*Options messages. We then use this
                field to populate the extensions when we build a descriptor, at which
                point all protos have been parsed and so all extensions are known.

                Extension numbers for custom options may be chosen as follows:

                -  For options which will only be used within a single application or
                   organization, or for experimental options, use field numbers 50000
                   through 99999. It is up to you to ensure that you do not use the same
                   number for multiple options.
                -  For options which will be published and used publicly by multiple
                   independent entities, e-mail
                   protobuf-global-extension-registry@google.com to reserve extension
                   numbers. Simply provide your project name (e.g. Objective-C plugin)
                   and your project website (if available) -- there's no need to explain
                   how you intend to use them. Usually you only need one extension
                   number. You can declare multiple options with only one extension
                   number by putting them in a sub-message. See the Custom Options
                   section of the docs for examples:
                   https://developers.google.com/protocol-buffers/docs/proto#options If
                   this turns out to be popular, a web service will be set up to
                   automatically assign option numbers.
            job (Union[dict, ~google.cloud.scheduler_v1beta1.types.Job]): The resource type. It must be in the format of
                {service_name}/{resource_type_kind}. The ``resource_type_kind`` must be
                singular and must not include version numbers.

                Example: ``storage.googleapis.com/Bucket``

                The value of the resource_type_kind must follow the regular expression
                /[A-Za-z][a-zA-Z0-9]+/. It should start with an upper case character and
                should use PascalCase (UpperCamelCase). The maximum number of characters
                allowed for the ``resource_type_kind`` is 100.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.scheduler_v1beta1.types.Job`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.scheduler_v1beta1.types.Job` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "create_job" not in self._inner_api_calls:
            self._inner_api_calls[
                "create_job"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.create_job,
                default_retry=self._method_configs["CreateJob"].retry,
                default_timeout=self._method_configs["CreateJob"].timeout,
                client_info=self._client_info,
            )

        request = cloudscheduler_pb2.CreateJobRequest(parent=parent, job=job)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["create_job"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def update_job(
        self,
        job,
        update_mask=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        A simple descriptor of a resource type.

        ResourceDescriptor annotates a resource message (either by means of a
        protobuf annotation or use in the service config), and associates the
        resource's schema, the resource type, and the pattern of the resource
        name.

        Example:

        ::

            message Topic {
              // Indicates this message defines a resource schema.
              // Declares the resource type in the format of {service}/{kind}.
              // For Kubernetes resources, the format is {api group}/{kind}.
              option (google.api.resource) = {
                type: "pubsub.googleapis.com/Topic"
                name_descriptor: {
                  pattern: "projects/{project}/topics/{topic}"
                  parent_type: "cloudresourcemanager.googleapis.com/Project"
                  parent_name_extractor: "projects/{project}"
                }
              };
            }

        The ResourceDescriptor Yaml config will look like:

        ::

            resources:
            - type: "pubsub.googleapis.com/Topic"
              name_descriptor:
                - pattern: "projects/{project}/topics/{topic}"
                  parent_type: "cloudresourcemanager.googleapis.com/Project"
                  parent_name_extractor: "projects/{project}"

        Sometimes, resources have multiple patterns, typically because they can
        live under multiple parents.

        Example:

        ::

            message LogEntry {
              option (google.api.resource) = {
                type: "logging.googleapis.com/LogEntry"
                name_descriptor: {
                  pattern: "projects/{project}/logs/{log}"
                  parent_type: "cloudresourcemanager.googleapis.com/Project"
                  parent_name_extractor: "projects/{project}"
                }
                name_descriptor: {
                  pattern: "folders/{folder}/logs/{log}"
                  parent_type: "cloudresourcemanager.googleapis.com/Folder"
                  parent_name_extractor: "folders/{folder}"
                }
                name_descriptor: {
                  pattern: "organizations/{organization}/logs/{log}"
                  parent_type: "cloudresourcemanager.googleapis.com/Organization"
                  parent_name_extractor: "organizations/{organization}"
                }
                name_descriptor: {
                  pattern: "billingAccounts/{billing_account}/logs/{log}"
                  parent_type: "billing.googleapis.com/BillingAccount"
                  parent_name_extractor: "billingAccounts/{billing_account}"
                }
              };
            }

        The ResourceDescriptor Yaml config will look like:

        ::

            resources:
            - type: 'logging.googleapis.com/LogEntry'
              name_descriptor:
                - pattern: "projects/{project}/logs/{log}"
                  parent_type: "cloudresourcemanager.googleapis.com/Project"
                  parent_name_extractor: "projects/{project}"
                - pattern: "folders/{folder}/logs/{log}"
                  parent_type: "cloudresourcemanager.googleapis.com/Folder"
                  parent_name_extractor: "folders/{folder}"
                - pattern: "organizations/{organization}/logs/{log}"
                  parent_type: "cloudresourcemanager.googleapis.com/Organization"
                  parent_name_extractor: "organizations/{organization}"
                - pattern: "billingAccounts/{billing_account}/logs/{log}"
                  parent_type: "billing.googleapis.com/BillingAccount"
                  parent_name_extractor: "billingAccounts/{billing_account}"

        For flexible resources, the resource name doesn't contain parent names,
        but the resource itself has parents for policy evaluation.

        Example:

        ::

            message Shelf {
              option (google.api.resource) = {
                type: "library.googleapis.com/Shelf"
                name_descriptor: {
                  pattern: "shelves/{shelf}"
                  parent_type: "cloudresourcemanager.googleapis.com/Project"
                }
                name_descriptor: {
                  pattern: "shelves/{shelf}"
                  parent_type: "cloudresourcemanager.googleapis.com/Folder"
                }
              };
            }

        The ResourceDescriptor Yaml config will look like:

        ::

            resources:
            - type: 'library.googleapis.com/Shelf'
              name_descriptor:
                - pattern: "shelves/{shelf}"
                  parent_type: "cloudresourcemanager.googleapis.com/Project"
                - pattern: "shelves/{shelf}"
                  parent_type: "cloudresourcemanager.googleapis.com/Folder"

        Example:
            >>> from google.cloud import scheduler_v1beta1
            >>>
            >>> client = scheduler_v1beta1.CloudSchedulerClient()
            >>>
            >>> # TODO: Initialize `job`:
            >>> job = {}
            >>>
            >>> response = client.update_job(job)

        Args:
            job (Union[dict, ~google.cloud.scheduler_v1beta1.types.Job]): The deadline for job attempts. If the request handler does not
                respond by this deadline then the request is cancelled and the attempt
                is marked as a ``DEADLINE_EXCEEDED`` failure. The failed attempt can be
                viewed in execution logs. Cloud Scheduler will retry the job according
                to the ``RetryConfig``.

                The allowed duration for this deadline is:

                -  For ``HTTP targets``, between 15 seconds and 30 minutes.
                -  For ``App Engine HTTP targets``, between 15 seconds and 24 hours.
                -  For ``PubSub targets``, this field is ignored.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.scheduler_v1beta1.types.Job`
            update_mask (Union[dict, ~google.cloud.scheduler_v1beta1.types.FieldMask]): A  mask used to specify which fields of the job are being updated.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.scheduler_v1beta1.types.FieldMask`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.scheduler_v1beta1.types.Job` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "update_job" not in self._inner_api_calls:
            self._inner_api_calls[
                "update_job"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.update_job,
                default_retry=self._method_configs["UpdateJob"].retry,
                default_timeout=self._method_configs["UpdateJob"].timeout,
                client_info=self._client_info,
            )

        request = cloudscheduler_pb2.UpdateJobRequest(job=job, update_mask=update_mask)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("job.name", job.name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["update_job"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def delete_job(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Deletes a job.

        Example:
            >>> from google.cloud import scheduler_v1beta1
            >>>
            >>> client = scheduler_v1beta1.CloudSchedulerClient()
            >>>
            >>> name = client.job_path('[PROJECT]', '[LOCATION]', '[JOB]')
            >>>
            >>> client.delete_job(name)

        Args:
            name (str): Signed seconds of the span of time. Must be from -315,576,000,000 to
                +315,576,000,000 inclusive. Note: these bounds are computed from: 60
                sec/min \* 60 min/hr \* 24 hr/day \* 365.25 days/year \* 10000 years
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "delete_job" not in self._inner_api_calls:
            self._inner_api_calls[
                "delete_job"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.delete_job,
                default_retry=self._method_configs["DeleteJob"].retry,
                default_timeout=self._method_configs["DeleteJob"].timeout,
                client_info=self._client_info,
            )

        request = cloudscheduler_pb2.DeleteJobRequest(name=name)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        self._inner_api_calls["delete_job"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def pause_job(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Request message for ``ResumeJob``.

        Example:
            >>> from google.cloud import scheduler_v1beta1
            >>>
            >>> client = scheduler_v1beta1.CloudSchedulerClient()
            >>>
            >>> name = client.job_path('[PROJECT]', '[LOCATION]', '[JOB]')
            >>>
            >>> response = client.pause_job(name)

        Args:
            name (str): Settings that determine the retry behavior.

                By default, if a job does not complete successfully (meaning that an
                acknowledgement is not received from the handler, then it will be
                retried with exponential backoff according to the settings in
                ``RetryConfig``.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.scheduler_v1beta1.types.Job` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "pause_job" not in self._inner_api_calls:
            self._inner_api_calls[
                "pause_job"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.pause_job,
                default_retry=self._method_configs["PauseJob"].retry,
                default_timeout=self._method_configs["PauseJob"].timeout,
                client_info=self._client_info,
            )

        request = cloudscheduler_pb2.PauseJobRequest(name=name)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["pause_job"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def resume_job(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        If set, gives the index of a oneof in the containing type's
        oneof_decl list. This field is a member of that oneof.

        Example:
            >>> from google.cloud import scheduler_v1beta1
            >>>
            >>> client = scheduler_v1beta1.CloudSchedulerClient()
            >>>
            >>> name = client.job_path('[PROJECT]', '[LOCATION]', '[JOB]')
            >>>
            >>> response = client.resume_job(name)

        Args:
            name (str): Required. The location name. For example:
                ``projects/PROJECT_ID/locations/LOCATION_ID``.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.scheduler_v1beta1.types.Job` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "resume_job" not in self._inner_api_calls:
            self._inner_api_calls[
                "resume_job"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.resume_job,
                default_retry=self._method_configs["ResumeJob"].retry,
                default_timeout=self._method_configs["ResumeJob"].timeout,
                client_info=self._client_info,
            )

        request = cloudscheduler_pb2.ResumeJobRequest(name=name)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["resume_job"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def run_job(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Forces a job to run now.

        When this method is called, Cloud Scheduler will dispatch the job, even
        if the job is already running.

        Example:
            >>> from google.cloud import scheduler_v1beta1
            >>>
            >>> client = scheduler_v1beta1.CloudSchedulerClient()
            >>>
            >>> name = client.job_path('[PROJECT]', '[LOCATION]', '[JOB]')
            >>>
            >>> response = client.run_job(name)

        Args:
            name (str): Denotes a field as required. This indicates that the field **must**
                be provided as part of the request, and failure to do so will cause an
                error (usually ``INVALID_ARGUMENT``).
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.scheduler_v1beta1.types.Job` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "run_job" not in self._inner_api_calls:
            self._inner_api_calls[
                "run_job"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.run_job,
                default_retry=self._method_configs["RunJob"].retry,
                default_timeout=self._method_configs["RunJob"].timeout,
                client_info=self._client_info,
            )

        request = cloudscheduler_pb2.RunJobRequest(name=name)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["run_job"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )
