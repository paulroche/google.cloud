#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2017 Google
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# ----------------------------------------------------------------------------
#
#     ***     AUTO GENERATED CODE    ***    Type: MMv1     ***
#
# ----------------------------------------------------------------------------
#
#     This file is automatically generated by Magic Modules and manual
#     changes will be clobbered when the file is regenerated.
#
#     Please read more about how to change this file at
#     https://www.github.com/GoogleCloudPlatform/magic-modules
#
# ----------------------------------------------------------------------------

from __future__ import absolute_import, division, print_function

__metaclass__ = type

################################################################################
# Documentation
################################################################################

ANSIBLE_METADATA = {'metadata_version': '1.1', 'status': ["preview"], 'supported_by': 'community'}

DOCUMENTATION = '''
---
module: gcp_cloudbuild_trigger_info
description:
- Gather info for GCP Trigger
short_description: Gather info for GCP Trigger
author: Google Inc. (@googlecloudplatform)
requirements:
- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0
options:
  project:
    description:
    - The Google Cloud Platform project to use.
    type: str
  auth_kind:
    description:
    - The type of credential used.
    type: str
    required: true
    choices:
    - application
    - machineaccount
    - serviceaccount
    - accesstoken
  service_account_contents:
    description:
    - The contents of a Service Account JSON file, either in a dictionary or as a
      JSON string that represents it.
    type: jsonarg
  service_account_file:
    description:
    - The path of a Service Account JSON file if serviceaccount is selected as type.
    type: path
  service_account_email:
    description:
    - An optional service account email address if machineaccount is selected and
      the user does not wish to use the default email.
    type: str
  access_token:
    description:
    - An OAuth2 access token if credential type is accesstoken.
    type: str
  scopes:
    description:
    - Array of scopes to be used
    type: list
    elements: str
  env_type:
    description:
    - Specifies which Ansible environment you're running this module within.
    - This should not be set unless you know what you're doing.
    - This only alters the User Agent string for any API requests.
    type: str
notes:
- for authentication, you can set service_account_file using the C(GCP_SERVICE_ACCOUNT_FILE)
  env variable.
- for authentication, you can set service_account_contents using the C(GCP_SERVICE_ACCOUNT_CONTENTS)
  env variable.
- For authentication, you can set service_account_email using the C(GCP_SERVICE_ACCOUNT_EMAIL)
  env variable.
- For authentication, you can set access_token using the C(GCP_ACCESS_TOKEN)
  env variable.
- For authentication, you can set auth_kind using the C(GCP_AUTH_KIND) env variable.
- For authentication, you can set scopes using the C(GCP_SCOPES) env variable.
- Environment variables values will only be used if the playbook values are not set.
- The I(service_account_email) and I(service_account_file) options are mutually exclusive.
'''

EXAMPLES = '''
- name: get info on a trigger
  gcp_cloudbuild_trigger_info:
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
'''

RETURN = '''
resources:
  description: List of resources
  returned: always
  type: complex
  contains:
    id:
      description:
      - The unique identifier for the trigger.
      returned: success
      type: str
    name:
      description:
      - Name of the trigger. Must be unique within the project.
      returned: success
      type: str
    description:
      description:
      - Human-readable description of the trigger.
      returned: success
      type: str
    tags:
      description:
      - Tags for annotation of a BuildTrigger .
      returned: success
      type: list
    disabled:
      description:
      - Whether the trigger is disabled or not. If true, the trigger will never result
        in a build.
      returned: success
      type: bool
    createTime:
      description:
      - Time when the trigger was created.
      returned: success
      type: str
    substitutions:
      description:
      - Substitutions data for Build resource.
      returned: success
      type: dict
    filename:
      description:
      - Path, from the source root, to a file whose contents is used for the template.
        Either a filename or build template must be provided.
      returned: success
      type: str
    ignoredFiles:
      description:
      - ignoredFiles and includedFiles are file glob matches using U(https://golang.org/pkg/path/filepath/#Match)
        extended with support for `**`.
      - If ignoredFiles and changed files are both empty, then they are not used to
        determine whether or not to trigger a build.
      - If ignoredFiles is not empty, then we ignore any files that match any of the
        ignored_file globs. If the change has no files that are outside of the ignoredFiles
        globs, then we do not trigger a build.
      returned: success
      type: list
    includedFiles:
      description:
      - ignoredFiles and includedFiles are file glob matches using U(https://golang.org/pkg/path/filepath/#Match)
        extended with support for `**`.
      - If any of the files altered in the commit pass the ignoredFiles filter and
        includedFiles is empty, then as far as this filter is concerned, we should
        trigger the build.
      - If any of the files altered in the commit pass the ignoredFiles filter and
        includedFiles is not empty, then we make sure that at least one of those files
        matches a includedFiles glob. If not, then we do not trigger a build.
      returned: success
      type: list
    triggerTemplate:
      description:
      - Template describing the types of source changes to trigger a build.
      - Branch and tag names in trigger templates are interpreted as regular expressions.
        Any branch or tag change that matches that regular expression will trigger
        a build.
      returned: success
      type: complex
      contains:
        projectId:
          description:
          - ID of the project that owns the Cloud Source Repository. If omitted, the
            project ID requesting the build is assumed.
          returned: success
          type: str
        repoName:
          description:
          - Name of the Cloud Source Repository. If omitted, the name "default" is
            assumed.
          returned: success
          type: str
        dir:
          description:
          - Directory, relative to the source root, in which to run the build.
          - This must be a relative path. If a step's dir is specified and is an absolute
            path, this value is ignored for that step's execution.
          returned: success
          type: str
        invertRegex:
          description:
          - Only trigger a build if the revision regex does NOT match the revision
            regex.
          returned: success
          type: bool
        branchName:
          description:
          - Name of the branch to build. Exactly one a of branch name, tag, or commit
            SHA must be provided.
          - This field is a regular expression.
          returned: success
          type: str
        tagName:
          description:
          - Name of the tag to build. Exactly one of a branch name, tag, or commit
            SHA must be provided.
          - This field is a regular expression.
          returned: success
          type: str
        commitSha:
          description:
          - Explicit commit SHA to build. Exactly one of a branch name, tag, or commit
            SHA must be provided.
          returned: success
          type: str
    github:
      description:
      - Describes the configuration of a trigger that creates a build whenever a GitHub
        event is received.
      returned: success
      type: complex
      contains:
        owner:
          description:
          - 'Owner of the repository. For example: The owner for U(https://github.com/googlecloudplatform/cloud-builders)
            is "googlecloudplatform".'
          returned: success
          type: str
        name:
          description:
          - 'Name of the repository. For example: The name for U(https://github.com/googlecloudplatform/cloud-builders)
            is "cloud-builders".'
          returned: success
          type: str
        pullRequest:
          description:
          - filter to match changes in pull requests. Specify only one of pullRequest
            or push.
          returned: success
          type: complex
          contains:
            branch:
              description:
              - Regex of branches to match.
              returned: success
              type: str
            commentControl:
              description:
              - Whether to block builds on a "/gcbrun" comment from a repository owner
                or collaborator.
              returned: success
              type: str
            invertRegex:
              description:
              - If true, branches that do NOT match the git_ref will trigger a build.
              returned: success
              type: bool
        push:
          description:
          - filter to match changes in refs, like branches or tags. Specify only one
            of pullRequest or push.
          returned: success
          type: complex
          contains:
            invertRegex:
              description:
              - When true, only trigger a build if the revision regex does NOT match
                the git_ref regex.
              returned: success
              type: bool
            branch:
              description:
              - Regex of branches to match. Specify only one of branch or tag.
              returned: success
              type: str
            tag:
              description:
              - Regex of tags to match. Specify only one of branch or tag.
              returned: success
              type: str
    pubsubConfig:
      description:
      - PubsubConfig describes the configuration of a trigger that creates a build
        whenever a Pub/Sub message is published.
      returned: success
      type: complex
      contains:
        subscription:
          description:
          - Output only. Name of the subscription.
          returned: success
          type: str
        topic:
          description:
          - The name of the topic from which this subscription is receiving messages.
          returned: success
          type: str
        service_account_email:
          description:
          - Service account that will make the push request.
          returned: success
          type: str
        state:
          description:
          - Potential issues with the underlying Pub/Sub subscription configuration.
          - Only populated on get requests.
          returned: success
          type: str
    webhookConfig:
      description:
      - WebhookConfig describes the configuration of a trigger that creates a build
        whenever a webhook is sent to a trigger's webhook URL.
      returned: success
      type: complex
      contains:
        secret:
          description:
          - Resource name for the secret required as a URL parameter.
          returned: success
          type: str
        state:
          description:
          - Potential issues with the underlying Pub/Sub subscription configuration.
          - Only populated on get requests.
          returned: success
          type: str
    build:
      description:
      - Contents of the build template. Either a filename or build template must be
        provided.
      returned: success
      type: complex
      contains:
        source:
          description:
          - The location of the source files to build.
          returned: success
          type: complex
          contains:
            storageSource:
              description:
              - Location of the source in an archive file in Google Cloud Storage.
              returned: success
              type: complex
              contains:
                bucket:
                  description:
                  - Google Cloud Storage bucket containing the source.
                  returned: success
                  type: str
                object:
                  description:
                  - Google Cloud Storage object containing the source.
                  - This object must be a gzipped archive file (.tar.gz) containing
                    source to build.
                  returned: success
                  type: str
                generation:
                  description:
                  - Google Cloud Storage generation for the object. If the generation
                    is omitted, the latest generation will be used .
                  returned: success
                  type: str
            repoSource:
              description:
              - Location of the source in a Google Cloud Source Repository.
              returned: success
              type: complex
              contains:
                projectId:
                  description:
                  - ID of the project that owns the Cloud Source Repository. If omitted,
                    the project ID requesting the build is assumed.
                  returned: success
                  type: str
                repoName:
                  description:
                  - Name of the Cloud Source Repository.
                  returned: success
                  type: str
                dir:
                  description:
                  - Directory, relative to the source root, in which to run the build.
                  - This must be a relative path. If a step's dir is specified and
                    is an absolute path, this value is ignored for that step's execution.
                  returned: success
                  type: str
                invertRegex:
                  description:
                  - Only trigger a build if the revision regex does NOT match the
                    revision regex.
                  returned: success
                  type: bool
                substitutions:
                  description:
                  - Substitutions to use in a triggered build. Should only be used
                    with triggers.run .
                  returned: success
                  type: dict
                branchName:
                  description:
                  - Regex matching branches to build. Exactly one a of branch name,
                    tag, or commit SHA must be provided.
                  - The syntax of the regular expressions accepted is the syntax accepted
                    by RE2 and described at U(https://github.com/google/re2/wiki/Syntax)
                    .
                  returned: success
                  type: str
                tagName:
                  description:
                  - Regex matching tags to build. Exactly one a of branch name, tag,
                    or commit SHA must be provided.
                  - The syntax of the regular expressions accepted is the syntax accepted
                    by RE2 and described at U(https://github.com/google/re2/wiki/Syntax)
                    .
                  returned: success
                  type: str
                commitSha:
                  description:
                  - Explicit commit SHA to build. Exactly one a of branch name, tag,
                    or commit SHA must be provided.
                  returned: success
                  type: str
        tags:
          description:
          - Tags for annotation of a Build. These are not docker tags.
          returned: success
          type: list
        images:
          description:
          - A list of images to be pushed upon the successful completion of all build
            steps.
          - The images are pushed using the builder service account's credentials.
          - The digests of the pushed images will be stored in the Build resource's
            results field.
          - If any of the images fail to be pushed, the build status is marked FAILURE.
          returned: success
          type: list
        substitutions:
          description:
          - Substitutions data for Build resource.
          returned: success
          type: dict
        queueTtl:
          description:
          - TTL in queue for this build. If provided and the build is enqueued longer
            than this value, the build will expire and the build status will be EXPIRED.
          - The TTL starts ticking from createTime.
          - 'A duration in seconds with up to nine fractional digits, terminated by
            ''s''. Example: "3.5s".'
          returned: success
          type: str
        logsBucket:
          description:
          - Google Cloud Storage bucket where logs should be written. Logs file names
            will be of the format ${logsBucket}/log-${build_id}.txt.
          returned: success
          type: str
        timeout:
          description:
          - Amount of time that this build should be allowed to run, to second granularity.
          - If this amount of time elapses, work on the build will cease and the build
            status will be TIMEOUT.
          - This timeout must be equal to or greater than the sum of the timeouts
            for build steps within the build.
          - The expected format is the number of seconds followed by s.
          - Default time is ten minutes (600s).
          returned: success
          type: str
        secrets:
          description:
          - Secrets to decrypt using Cloud Key Management Service.
          returned: success
          type: complex
          contains:
            kmsKeyName:
              description:
              - Cloud KMS key name to use to decrypt these envs.
              returned: success
              type: str
            secretEnv:
              description:
              - Map of environment variable name to its encrypted value.
              - Secret environment variables must be unique across all of a build's
                secrets, and must be used by at least one build step. Values can be
                at most 64 KB in size. There can be at most 100 secret values across
                all of a build's secrets.
              returned: success
              type: dict
        steps:
          description:
          - The operations to be performed on the workspace.
          returned: success
          type: complex
          contains:
            name:
              description:
              - The name of the container image that will run this particular build
                step.
              - If the image is available in the host's Docker daemon's cache, it
                will be run directly. If not, the host will attempt to pull the image
                first, using the builder service account's credentials if necessary.
              - The Docker daemon's cache will already have the latest versions of
                all of the officially supported build steps (see U(https://github.com/GoogleCloudPlatform/cloud-builders)
                for images and examples).
              - The Docker daemon will also have cached many of the layers for some
                popular images, like "ubuntu", "debian", but they will be refreshed
                at the time you attempt to use them.
              - If you built an image in a previous build step, it will be stored
                in the host's Docker daemon's cache and is available to use as the
                name for a later build step.
              returned: success
              type: str
            args:
              description:
              - A list of arguments that will be presented to the step when it is
                started.
              - If the image used to run the step's container has an entrypoint, the
                args are used as arguments to that entrypoint. If the image does not
                define an entrypoint, the first element in args is used as the entrypoint,
                and the remainder will be used as arguments.
              returned: success
              type: list
            env:
              description:
              - A list of environment variable definitions to be used when running
                a step.
              - The elements are of the form "KEY=VALUE" for the environment variable
                "KEY" being given the value "VALUE".
              returned: success
              type: list
            id:
              description:
              - Unique identifier for this build step, used in `wait_for` to reference
                this build step as a dependency.
              returned: success
              type: str
            entrypoint:
              description:
              - Entrypoint to be used instead of the build step image's default entrypoint.
              - If unset, the image's default entrypoint is used .
              returned: success
              type: str
            dir:
              description:
              - Working directory to use when running this step's container.
              - If this value is a relative path, it is relative to the build's working
                directory. If this value is absolute, it may be outside the build's
                working directory, in which case the contents of the path may not
                be persisted across build step executions, unless a `volume` for that
                path is specified.
              - If the build specifies a `RepoSource` with `dir` and a step with a
                `dir`, which specifies an absolute path, the `RepoSource` `dir` is
                ignored for the step's execution.
              returned: success
              type: str
            secretEnv:
              description:
              - A list of environment variables which are encrypted using a Cloud
                Key Management Service crypto key. These values must be specified
                in the build's `Secret`.
              returned: success
              type: list
            timeout:
              description:
              - Time limit for executing this build step. If not defined, the step
                has no time limit and will be allowed to continue to run until either
                it completes or the build itself times out.
              returned: success
              type: str
            timing:
              description:
              - Output only. Stores timing information for executing this build step.
              returned: success
              type: str
            volumes:
              description:
              - List of volumes to mount into the build step.
              - Each volume is created as an empty volume prior to execution of the
                build step. Upon completion of the build, volumes and their contents
                are discarded.
              - Using a named volume in only one step is not valid as it is indicative
                of a build request with an incorrect configuration.
              returned: success
              type: complex
              contains:
                name:
                  description:
                  - Name of the volume to mount.
                  - Volume names must be unique per build step and must be valid names
                    for Docker volumes. Each named volume must be used by at least
                    two build steps.
                  returned: success
                  type: str
                path:
                  description:
                  - Path at which to mount the volume.
                  - Paths must be absolute and cannot conflict with other volume paths
                    on the same build step or with certain reserved volume paths.
                  returned: success
                  type: str
            waitFor:
              description:
              - The ID(s) of the step(s) that this build step depends on.
              - This build step will not start until all the build steps in `wait_for`
                have completed successfully. If `wait_for` is empty, this build step
                will start when all previous build steps in the `Build.Steps` list
                have completed successfully.
              returned: success
              type: list
        artifacts:
          description:
          - Artifacts produced by the build that should be uploaded upon successful
            completion of all build steps.
          returned: success
          type: complex
          contains:
            images:
              description:
              - A list of images to be pushed upon the successful completion of all
                build steps.
              - The images will be pushed using the builder service account's credentials.
              - The digests of the pushed images will be stored in the Build resource's
                results field.
              - If any of the images fail to be pushed, the build is marked FAILURE.
              returned: success
              type: list
            objects:
              description:
              - A list of objects to be uploaded to Cloud Storage upon successful
                completion of all build steps.
              - Files in the workspace matching specified paths globs will be uploaded
                to the Cloud Storage location using the builder service account's
                credentials.
              - The location and generation of the uploaded objects will be stored
                in the Build resource's results field.
              - If any objects fail to be pushed, the build is marked FAILURE.
              returned: success
              type: complex
              contains:
                location:
                  description:
                  - Cloud Storage bucket and optional object path, in the form "gs://bucket/path/to/somewhere/".
                  - Files in the workspace matching any path pattern will be uploaded
                    to Cloud Storage with this location as a prefix.
                  returned: success
                  type: str
                paths:
                  description:
                  - Path globs used to match files in the build's workspace.
                  returned: success
                  type: list
                timing:
                  description:
                  - Output only. Stores timing information for pushing all artifact
                    objects.
                  returned: success
                  type: complex
                  contains:
                    startTime:
                      description:
                      - Start of time span.
                      - 'A timestamp in RFC3339 UTC "Zulu" format, with nanosecond
                        resolution and up to nine fractional digits. Examples: "2014-10-02T15:01:23Z"
                        and "2014-10-02T15:01:23.045123456Z".'
                      returned: success
                      type: str
                    endTime:
                      description:
                      - End of time span.
                      - 'A timestamp in RFC3339 UTC "Zulu" format, with nanosecond
                        resolution and up to nine fractional digits. Examples: "2014-10-02T15:01:23Z"
                        and "2014-10-02T15:01:23.045123456Z".'
                      returned: success
                      type: str
        options:
          description:
          - Special options for this build.
          returned: success
          type: complex
          contains:
            sourceProvenanceHash:
              description:
              - Requested hash for SourceProvenance.
              returned: success
              type: list
            requestedVerifyOption:
              description:
              - Requested verifiability options.
              returned: success
              type: str
            machineType:
              description:
              - Compute Engine machine type on which to run the build.
              returned: success
              type: str
            diskSizeGb:
              description:
              - Requested disk size for the VM that runs the build. Note that this
                is NOT "disk free"; some of the space will be used by the operating
                system and build utilities.
              - Also note that this is the minimum disk size that will be allocated
                for the build -- the build may run with a larger disk than requested.
                At present, the maximum disk size is 1000GB; builds that request more
                than the maximum are rejected with an error.
              returned: success
              type: int
            substitutionOption:
              description:
              - Option to specify behavior when there is an error in the substitution
                checks.
              - NOTE this is always set to ALLOW_LOOSE for triggered builds and cannot
                be overridden in the build configuration file.
              returned: success
              type: str
            dynamicSubstitutions:
              description:
              - Option to specify whether or not to apply bash style string operations
                to the substitutions.
              - NOTE this is always enabled for triggered builds and cannot be overridden
                in the build configuration file.
              returned: success
              type: bool
            logStreamingOption:
              description:
              - Option to define build log streaming behavior to Google Cloud Storage.
              returned: success
              type: str
            workerPool:
              description:
              - Option to specify a WorkerPool for the build. Format projects/{project}/workerPools/{workerPool}
                This field is experimental.
              returned: success
              type: str
            logging:
              description:
              - Option to specify the logging mode, which determines if and where
                build logs are stored.
              returned: success
              type: str
            env:
              description:
              - A list of global environment variable definitions that will exist
                for all build steps in this build. If a variable is defined in both
                globally and in a build step, the variable will use the build step
                value.
              - The elements are of the form "KEY=VALUE" for the environment variable
                "KEY" being given the value "VALUE".
              returned: success
              type: list
            secretEnv:
              description:
              - A list of global environment variables, which are encrypted using
                a Cloud Key Management Service crypto key. These values must be specified
                in the build's Secret. These variables will be available to all build
                steps in this build.
              returned: success
              type: list
            volumes:
              description:
              - Global list of volumes to mount for ALL build steps Each volume is
                created as an empty volume prior to starting the build process.
              - Upon completion of the build, volumes and their contents are discarded.
                Global volume names and paths cannot conflict with the volumes defined
                a build step.
              - Using a global volume in a build with only one step is not valid as
                it is indicative of a build request with an incorrect configuration.
              returned: success
              type: complex
              contains:
                name:
                  description:
                  - Name of the volume to mount.
                  - Volume names must be unique per build step and must be valid names
                    for Docker volumes.
                  - Each named volume must be used by at least two build steps.
                  returned: success
                  type: str
                path:
                  description:
                  - Path at which to mount the volume.
                  - Paths must be absolute and cannot conflict with other volume paths
                    on the same build step or with certain reserved volume paths.
                  returned: success
                  type: str
'''

################################################################################
# Imports
################################################################################
from ansible_collections.google.cloud.plugins.module_utils.gcp_utils import navigate_hash, GcpSession, GcpModule
import json

################################################################################
# Main
################################################################################


def main():
    module = GcpModule(argument_spec=dict())

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/cloud-platform']

    return_value = {'resources': fetch_list(module, collection(module))}
    module.exit_json(**return_value)


def collection(module):
    return "https://cloudbuild.googleapis.com/v1/projects/{project}/triggers".format(**module.params)


def fetch_list(module, link):
    auth = GcpSession(module, 'cloudbuild')
    return auth.list(link, return_if_object, array_name='triggers')


def return_if_object(module, response):
    # If not found, return nothing.
    if response.status_code == 404:
        return None

    # If no content, return nothing.
    if response.status_code == 204:
        return None

    try:
        module.raise_for_status(response)
        result = response.json()
    except getattr(json.decoder, 'JSONDecodeError', ValueError) as inst:
        module.fail_json(msg="Invalid JSON response with error: %s" % inst)

    if navigate_hash(result, ['error', 'errors']):
        module.fail_json(msg=navigate_hash(result, ['error', 'errors']))

    return result


if __name__ == "__main__":
    main()
