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


import google.api_core.grpc_helpers

from google.cloud.scheduler_v1.proto import cloudscheduler_pb2_grpc


class CloudSchedulerGrpcTransport(object):
    """gRPC transport class providing stubs for
    google.cloud.scheduler.v1 CloudScheduler API.

    The transport provides access to the raw gRPC stubs,
    which can be used to take advantage of advanced
    features of gRPC.
    """

    # The scopes needed to make gRPC calls to all of the methods defined
    # in this service.
    _OAUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    def __init__(
        self,
        channel=None,
        credentials=None,
        address="cloudscheduler.googleapis.com:443",
    ):
        """Instantiate the transport class.

        Args:
            channel (grpc.Channel): A ``Channel`` instance through
                which to make calls. This argument is mutually exclusive
                with ``credentials``; providing both will raise an exception.
            credentials (google.auth.credentials.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            address (str): The address where the service is hosted.
        """
        # If both `channel` and `credentials` are specified, raise an
        # exception (channels come with credentials baked in already).
        if channel is not None and credentials is not None:
            raise ValueError(
                "The `channel` and `credentials` arguments are mutually " "exclusive."
            )

        # Create the channel.
        if channel is None:
            channel = self.create_channel(
                address=address,
                credentials=credentials,
                options={
                    "grpc.max_send_message_length": -1,
                    "grpc.max_receive_message_length": -1,
                }.items(),
            )

        self._channel = channel

        # gRPC uses objects called "stubs" that are bound to the
        # channel and provide a basic method for each RPC.
        self._stubs = {
            "cloud_scheduler_stub": cloudscheduler_pb2_grpc.CloudSchedulerStub(channel)
        }

    @classmethod
    def create_channel(
        cls, address="cloudscheduler.googleapis.com:443", credentials=None, **kwargs
    ):
        """Create and return a gRPC channel object.

        Args:
            address (str): The host for the channel to use.
            credentials (~.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            kwargs (dict): Keyword arguments, which are passed to the
                channel creation.

        Returns:
            grpc.Channel: A gRPC channel object.
        """
        return google.api_core.grpc_helpers.create_channel(
            address, credentials=credentials, scopes=cls._OAUTH_SCOPES, **kwargs
        )

    @property
    def channel(self):
        """The gRPC channel used by the transport.

        Returns:
            grpc.Channel: A gRPC channel object.
        """
        return self._channel

    @property
    def list_jobs(self):
        """Return the gRPC stub for :meth:`CloudSchedulerClient.list_jobs`.

        Lists jobs.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["cloud_scheduler_stub"].ListJobs

    @property
    def get_job(self):
        """Return the gRPC stub for :meth:`CloudSchedulerClient.get_job`.

        Gets a job.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["cloud_scheduler_stub"].GetJob

    @property
    def create_job(self):
        """Return the gRPC stub for :meth:`CloudSchedulerClient.create_job`.

        Creates a job.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["cloud_scheduler_stub"].CreateJob

    @property
    def update_job(self):
        """Return the gRPC stub for :meth:`CloudSchedulerClient.update_job`.

        App Engine Routing.

        For more information about services, versions, and instances see `An
        Overview of App
        Engine <https://cloud.google.com/appengine/docs/python/an-overview-of-app-engine>`__,
        `Microservices Architecture on Google App
        Engine <https://cloud.google.com/appengine/docs/python/microservices-on-app-engine>`__,
        `App Engine Standard request
        routing <https://cloud.google.com/appengine/docs/standard/python/how-requests-are-routed>`__,
        and `App Engine Flex request
        routing <https://cloud.google.com/appengine/docs/flexible/python/how-requests-are-routed>`__.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["cloud_scheduler_stub"].UpdateJob

    @property
    def delete_job(self):
        """Return the gRPC stub for :meth:`CloudSchedulerClient.delete_job`.

        Deletes a job.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["cloud_scheduler_stub"].DeleteJob

    @property
    def pause_job(self):
        """Return the gRPC stub for :meth:`CloudSchedulerClient.pause_job`.

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

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["cloud_scheduler_stub"].PauseJob

    @property
    def resume_job(self):
        """Return the gRPC stub for :meth:`CloudSchedulerClient.resume_job`.

        If set, gives the index of a oneof in the containing type's
        oneof_decl list. This field is a member of that oneof.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["cloud_scheduler_stub"].ResumeJob

    @property
    def run_job(self):
        """Return the gRPC stub for :meth:`CloudSchedulerClient.run_job`.

        Forces a job to run now.

        When this method is called, Cloud Scheduler will dispatch the job, even
        if the job is already running.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["cloud_scheduler_stub"].RunJob
