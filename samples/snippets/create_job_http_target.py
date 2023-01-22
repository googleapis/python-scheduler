# Copyright 2022 sjha200000@gmail.com

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.



def create_scheduler_job_http_target(project_id, location_id, service_id):
    """Create a job with an App Engine target via the Cloud Scheduler API"""
    # [START cloud_scheduler_create_job]
    from google.cloud import scheduler

    # Create a client.
    client = scheduler.CloudSchedulerClient()

    # TODO(developer): Uncomment and set the following variables
    # project_id = 'PROJECT_ID'
    # location_id = 'LOCATION_ID'
    
    # TODO(developer): Add your service URL
    uri = 'SERVICE_URL'
    
    # Construct the fully qualified location path.
    parent = f"projects/{project_id}/locations/{location_id}"

    headers = {
    "Content-Type": "application/json"
    }
    body ='{"test_key":"test_value"}'

    # Construct the request body.
    job = {
        "http_target":{
            "uri": uri,
            "http_method": 'POST',
            "headers": headers,
            "body": body.encode()
        },
        "schedule": "0 */3 * * * ",
        "time_zone": "Asia/Calcutta",
    }

    # Use the client to send the job creation request.
    response = client.create_job(request={"parent": parent, "job": job})

    print("Created job: {}".format(response.name))
    # [END cloud_scheduler_create_job]
    return response

