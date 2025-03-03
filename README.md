# log10py

<div align="left">
    <a href="https://speakeasyapi.dev/"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>


## 🏗 **Welcome to your new SDK!** 🏗

It has been generated successfully based on your OpenAPI spec. However, it is not yet ready for production use. Here are some next steps:
- [ ] 🛠 Make your SDK feel handcrafted by [customizing it](https://www.speakeasyapi.dev/docs/customize-sdks)
- [ ] ♻️ Refine your SDK quickly by iterating locally with the [Speakeasy CLI](https://github.com/speakeasy-api/speakeasy)
- [ ] 🎁 Publish your SDK to package managers by [configuring automatic publishing](https://www.speakeasyapi.dev/docs/advanced-setup/publish-sdks)
- [ ] ✨ When ready to productionize, delete this section from the README

<!-- Start Summary [summary] -->
## Summary

Log10 Feedback API Spec: Log10 Feedback API Spec
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [log10py](#log10py)
  * [🏗 **Welcome to your new SDK!** 🏗](#welcome-to-your-new-sdk)
  * [SDK Installation](#sdk-installation)
  * [SDK Example Usage](#sdk-example-usage)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Authentication](#authentication)
* [Development](#development)
  * [Maturity](#maturity)
  * [Contributions](#contributions)
* [log10py](#log10py-1)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

The SDK can be installed using the *pip* package manager, with dependencies and metadata stored in the `setup.py` file.

```bash
pip install log10py
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
import log10

s = log10.Log10(
    log10_token='<YOUR_API_KEY_HERE>',
)


res = s.sessions.create(x_log10_organization='<value>')

if res.object is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [completions](docs/sdks/completions/README.md)

* [create](docs/sdks/completions/README.md#create) - Create a completion
* [update](docs/sdks/completions/README.md#update) - Update completion by id.
* [list_ungraded](docs/sdks/completions/README.md#list_ungraded) - List ungraded completions i.e. completions that have not been associated with feedback but matches task selector.

### [feedback](docs/sdks/feedback/README.md)

* [get](docs/sdks/feedback/README.md#get) - Fetch feedback by id.
* [list](docs/sdks/feedback/README.md#list) - List feedback
* [upload](docs/sdks/feedback/README.md#upload) - Upload a piece of feedback

### [feedback_tasks](docs/sdks/feedbacktasks/README.md)

* [list](docs/sdks/feedbacktasks/README.md#list) - List feedback tasks.
* [create](docs/sdks/feedbacktasks/README.md#create) - Create a new task.
* [get](docs/sdks/feedbacktasks/README.md#get) - Retrieves feedback task `taskId`.


### [sessions](docs/sdks/sessions/README.md)

* [create](docs/sdks/sessions/README.md#create) - Create a session

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations. All operations return a response object or raise an exception.

By default, an API error will raise a errors.SDKError exception, which has the following properties:

| Property        | Type             | Description           |
|-----------------|------------------|-----------------------|
| `.status_code`  | *int*            | The HTTP status code  |
| `.message`      | *str*            | The error message     |
| `.raw_response` | *httpx.Response* | The raw HTTP response |
| `.body`         | *str*            | The response content  |

When custom error responses are specified for an operation, the SDK may also raise their associated exception. You can refer to respective *Errors* tables in SDK docs for more details on possible exception types for each operation. For example, the `create` method may raise the following exceptions:

| Error Type      | Status Code | Content Type |
| --------------- | ----------- | ------------ |
| errors.SDKError | 4XX, 5XX    | \*/\*        |

### Example

```python
import log10
from log10.models import components, errors

s = log10.Log10(
    log10_token='<YOUR_API_KEY_HERE>',
)

res = None
try:
    res = s.completions.create(completion=components.Completion(
    organization_id='<id>',
    request=components.CreateChatCompletionRequest(
        messages=[
            components.ChatCompletionRequestToolMessage(
                role=components.ChatCompletionRole.ASSISTANT,
                content='<value>',
                tool_call_id='<id>',
            ),
        ],
        model='gpt-4-turbo',
        response_format=components.ResponseFormat(),
        user='user-1234',
    ),
    response=components.CreateChatCompletionResponse(
        id='<id>',
        choices=[

        ],
        created=69025,
        model='gpt-4-turbo',
        object=components.Object.CHAT_COMPLETION,
    ),
), x_log10_organization='<value>')

except errors.SDKError as e:
    # handle exception
    raise(e)

if res.any is not None:
    # handle response
    pass

```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Override Server URL Per-Client

The default server can be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import log10
from log10.models import components

s = log10.Log10(
    server_url='https://log10.io',
    log10_token='<YOUR_API_KEY_HERE>',
)


res = s.completions.create(completion=components.Completion(
    organization_id='<id>',
    request=components.CreateChatCompletionRequest(
        messages=[
            components.ChatCompletionRequestToolMessage(
                role=components.ChatCompletionRole.ASSISTANT,
                content='<value>',
                tool_call_id='<id>',
            ),
        ],
        model='gpt-4-turbo',
        response_format=components.ResponseFormat(),
        user='user-1234',
    ),
    response=components.CreateChatCompletionResponse(
        id='<id>',
        choices=[

        ],
        created=69025,
        model='gpt-4-turbo',
        object=components.Object.CHAT_COMPLETION,
    ),
), x_log10_organization='<value>')

if res.any is not None:
    # handle response
    pass

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [requests](https://pypi.org/project/requests/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import log10
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = log10.Log10(client=http_client)
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name          | Type   | Scheme  |
| ------------- | ------ | ------- |
| `log10_token` | apiKey | API key |

To authenticate with the API the `log10_token` parameter must be set when initializing the SDK client instance. For example:
```python
import log10
from log10.models import components

s = log10.Log10(
    log10_token='<YOUR_API_KEY_HERE>',
)


res = s.completions.create(completion=components.Completion(
    organization_id='<id>',
    request=components.CreateChatCompletionRequest(
        messages=[
            components.ChatCompletionRequestToolMessage(
                role=components.ChatCompletionRole.ASSISTANT,
                content='<value>',
                tool_call_id='<id>',
            ),
        ],
        model='gpt-4-turbo',
        response_format=components.ResponseFormat(),
        user='user-1234',
    ),
    response=components.CreateChatCompletionResponse(
        id='<id>',
        choices=[

        ],
        created=69025,
        model='gpt-4-turbo',
        object=components.Object.CHAT_COMPLETION,
    ),
), x_log10_organization='<value>')

if res.any is not None:
    # handle response
    pass

```
<!-- End Authentication [security] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
# log10py
