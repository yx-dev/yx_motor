# Welcome to yx_motor
> Python client library for Alteryx Analytics Hub.  This is very early development, and the AAH API is still in preview mode. Do not consider this library stable until it is directly stated in the documentation.


## Installing 

Not ready yet.  Will update when we are ready to create a pip module.  The command will be the following once this is ready:

`pip install yx_motor`

## Development Installation

Clone this branch down to your machine.

Create a virtual environment in your venv manager of choice.  Activate the environment, navigate to this directory, and then run `pip install -e .` 

## Examples

### Initialize Client

```python
from yx_motor.client import Client

from private import server_vars

base_url = server_vars['base_url']
login_email = server_vars['login_email']
login_pwd = server_vars['login_pwd']

example_client = Client(base_url,
                        login_email,
                        login_pwd)
```

    POST sent to: https://hub-beta.demo.alteryx.com/api/v1/authenticate/
    with headers: {'User-Agent': 'python-requests/2.23.0', 'Accept-Encoding': 'gzip,deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Accept-Language': 'en-US,en;q=0.5', 'Content-Length': '57'}
    Response Status: 200
    

### View Jobs

```python
jobs_api_response = example_client.jobs.get_job()
```

    GET sent to: https://hub-beta.demo.alteryx.com/api/v1/jobs/
    with headers: {'User-Agent': 'python-requests/2.23.0', 'Accept-Encoding': 'gzip,deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Accept-Language': 'en-US,en;q=0.5', 'Cookie': 'ayxSession=s%3A44afbe59-8af5-4917-8290-ec987d0a1e56.TEd0guEXnm%2FCfQMTtkJw8g1WvWbobeFi%2FfkXcO4dvuo'}
    Response Status: 200
    

```python
jobs_api_response.json()['jobs'][0].keys()
```




    dict_keys(['jobId', 'workerId', 'scheduleId', 'executionOrdinal', 'queuedDate', 'scheduledStartDate', 'actualStartDate', 'completionDate', 'runTime', 'status', 'result', 'siteId', 'creationDate', 'lastUpdate', 'assetVersion', 'retryCount', 'notes', 'priority', 'jobNo', 'runStatus', 'name', 'userId', 'assetId', 'type', 'frequencyInterval', 'outputs'])



### Download and Upload Files

```python
file_a_uuid = file_a['uuid']
file_b_uuid = file_b['uuid']

files = example_client.files

response_a = files.download_file(file_uuid=file_a_uuid,
                               download_path=f"example_downloads/file_a.yxmd")

response_b = files.download_file(file_uuid=file_b_uuid,
                               download_path=f"example_downloads/file_b.yxmd")
```

    GET sent to: https://hub-beta.demo.alteryx.com/api/v1/files/content?id=cd68ff45-fc21-4a32-b2e9-8d5b85881b7e
    with headers: {'User-Agent': 'python-requests/2.23.0', 'Accept-Encoding': 'gzip,deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Accept-Language': 'en-US,en;q=0.5', 'Cookie': 'ayxSession=s%3A44afbe59-8af5-4917-8290-ec987d0a1e56.TEd0guEXnm%2FCfQMTtkJw8g1WvWbobeFi%2FfkXcO4dvuo'}
    Response Status: 200
    GET sent to: https://hub-beta.demo.alteryx.com/api/v1/files/content?id=8d346ce1-98b7-4729-a2d4-312fe980a861
    with headers: {'User-Agent': 'python-requests/2.23.0', 'Accept-Encoding': 'gzip,deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Accept-Language': 'en-US,en;q=0.5', 'Cookie': 'ayxSession=s%3A44afbe59-8af5-4917-8290-ec987d0a1e56.TEd0guEXnm%2FCfQMTtkJw8g1WvWbobeFi%2FfkXcO4dvuo'}
    Response Status: 200
    

### Trigger Workflows and Fetch Results

```python
run_workflow_response = example_client.workflows.run_workflow(
    asset_id=file_a_uuid,
    schedule_name='aah api trigger workflow'
)
```

    POST sent to: https://hub-beta.demo.alteryx.com/api/v1/workflows/run
    with headers: {'User-Agent': 'python-requests/2.23.0', 'Accept-Encoding': 'gzip,deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Accept-Language': 'en-US,en;q=0.5', 'Cookie': 'ayxSession=s%3A44afbe59-8af5-4917-8290-ec987d0a1e56.TEd0guEXnm%2FCfQMTtkJw8g1WvWbobeFi%2FfkXcO4dvuo', 'Content-Length': '101'}
    Response Status: 200
    

```python
run_workflow_response.json()['status']
```




    'active'



```python
schedule_id = run_workflow_response.json()['scheduleId']
```

```python
output_path = f"example_downloads/workflow_results.csv"

download_workflow_results_response = example_client.workflows.download_workflow_results(
    schedule_id=schedule_id, 
    download_path=output_path
)
```

    GET sent to: https://hub-beta.demo.alteryx.com/api/v1/jobs/?scheduleId=231fc776-4112-47af-9d5a-ca147e81b7ad
    with headers: {'User-Agent': 'python-requests/2.23.0', 'Accept-Encoding': 'gzip,deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Accept-Language': 'en-US,en;q=0.5', 'Cookie': 'ayxSession=s%3A44afbe59-8af5-4917-8290-ec987d0a1e56.TEd0guEXnm%2FCfQMTtkJw8g1WvWbobeFi%2FfkXcO4dvuo'}
    Response Status: 200
    GET sent to: https://hub-beta.demo.alteryx.com/api/v1/files/content?id=0214dd72-e846-40a7-923c-0e6c47b78b5f
    with headers: {'User-Agent': 'python-requests/2.23.0', 'Accept-Encoding': 'gzip,deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Accept-Language': 'en-US,en;q=0.5', 'Cookie': 'ayxSession=s%3A44afbe59-8af5-4917-8290-ec987d0a1e56.TEd0guEXnm%2FCfQMTtkJw8g1WvWbobeFi%2FfkXcO4dvuo'}
    Response Status: 200
    
