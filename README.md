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

<!-- Start SDK Installation [installation] -->
## SDK Installation

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
    log10_token="<YOUR_API_KEY_HERE>",
)


res = s.sessions.create(x_log10_organization='<value>')

if res.object is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [completions](docs/sdks/completions/README.md)

* [create](docs/sdks/completions/README.md#create) - Create a completion
* [update](docs/sdks/completions/README.md#update) - Update completion by id.
* [list_ungraded](docs/sdks/completions/README.md#list_ungraded) - List ungraded completions i.e. completions that have not been associated with feedback but matches task selector.

### [sessions](docs/sdks/sessions/README.md)

* [create](docs/sdks/sessions/README.md#create) - Create a session

### [feedback](docs/sdks/feedback/README.md)

* [get](docs/sdks/feedback/README.md#get) - Fetch feedback by id.
* [list](docs/sdks/feedback/README.md#list) - List feedback
* [upload](docs/sdks/feedback/README.md#upload) - Upload a piece of feedback

### [feedback_tasks](docs/sdks/feedbacktasks/README.md)

* [list](docs/sdks/feedbacktasks/README.md#list) - List feedback tasks.
* [create](docs/sdks/feedbacktasks/README.md#create) - Create a new task.
* [get](docs/sdks/feedbacktasks/README.md#get) - Retrieves feedback task `taskId`.
<!-- End Available Resources and Operations [operations] -->

<!-- Start Global Parameters [global-parameters] -->
## Global Parameters

A parameter is configured globally. This parameter may be set on the SDK client instance itself during initialization. When configured as an option during SDK initialization, This global value will be used as the default on the operations that use it. When such operations are called, there is a place in each to override the global value, if needed.

For example, you can set `X-Log10-Organization` to `'<value>'` at SDK initialization and then you do not have to pass the same value on calls to operations like `update`. But if you want to do so you may, which will locally override the global setting. See the example code below for a demonstration.


### Available Globals

The following global parameter is available.

| Name | Type | Required | Description |
| ---- | ---- |:--------:| ----------- |
| x_log10_organization | str |  | The x_log10_organization parameter. |


### Example

```python
import log10
from log10.models import components

s = log10.Log10(
    log10_token="<YOUR_API_KEY_HERE>",
)


res = s.completions.update(completion_id='<value>', completion=components.Completion(
    organization_id='<value>',
    request=components.CreateChatCompletionRequest(
        messages=[
            components.ChatCompletionRequestFunctionMessage(
                role=components.ChatCompletionRole.SYSTEM,
                content='<value>',
                name='<value>',
            ),
        ],
        model='gpt-4-turbo',
        n=1,
        response_format=components.ResponseFormat(
            type=components.CreateChatCompletionRequestType.JSON_OBJECT,
        ),
        temperature=1,
        top_p=1,
        user='user-1234',
    ),
    response=components.CreateChatCompletionResponse(
        id='<id>',
        choices=[
            components.Choices(
                finish_reason=components.FinishReason.TOOL_CALLS,
                index=15652,
                message=components.ChatCompletionResponseMessage(
                    content='<value>',
                    role=components.ChatCompletionRole.USER,
                ),
                logprobs=components.Logprobs(
                    content=[
                        components.ChatCompletionTokenLogprob(
                            token='<value>',
                            logprob=7084.55,
                            bytes=[
                                991464,
                            ],
                            top_logprobs=[
                                components.TopLogprobs(
                                    token='<value>',
                                    logprob=2703.24,
                                    bytes=[
                                        627690,
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
            ),
        ],
        created=684199,
        model='gpt-4-turbo',
        object=components.Object.CHAT_COMPLETION,
    ),
), x_log10_organization='<value>')

if res.completion is not None:
    # handle response
    pass

```
<!-- End Global Parameters [global-parameters] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

### Example

```python
import log10
from log10.models import components, errors

s = log10.Log10(
    log10_token="<YOUR_API_KEY_HERE>",
)

res = None
try:
    res = s.completions.create(completion=components.Completion(
    organization_id='<value>',
    request=components.CreateChatCompletionRequest(
        messages=[
            components.ChatCompletionRequestAssistantMessage(
                role=components.ChatCompletionRole.ASSISTANT,
            ),
        ],
        model='gpt-4-turbo',
        n=1,
        response_format=components.ResponseFormat(
            type=components.CreateChatCompletionRequestType.JSON_OBJECT,
        ),
        temperature=1,
        top_p=1,
        user='user-1234',
    ),
    response=components.CreateChatCompletionResponse(
        id='<id>',
        choices=[
            components.Choices(
                finish_reason=components.FinishReason.CONTENT_FILTER,
                index=859213,
                message=components.ChatCompletionResponseMessage(
                    content='<value>',
                    role=components.ChatCompletionRole.ASSISTANT,
                ),
                logprobs=components.Logprobs(
                    content=[
                        components.ChatCompletionTokenLogprob(
                            token='<value>',
                            logprob=2884.08,
                            bytes=[
                                134365,
                            ],
                            top_logprobs=[
                                components.TopLogprobs(
                                    token='<value>',
                                    logprob=7865.46,
                                    bytes=[
                                        69025,
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
            ),
        ],
        created=996706,
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

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://log10.io` | None |

#### Example

```python
import log10
from log10.models import components

s = log10.Log10(
    server_idx=0,
    log10_token="<YOUR_API_KEY_HERE>",
)


res = s.completions.create(completion=components.Completion(
    organization_id='<value>',
    request=components.CreateChatCompletionRequest(
        messages=[
            components.ChatCompletionRequestAssistantMessage(
                role=components.ChatCompletionRole.ASSISTANT,
            ),
        ],
        model='gpt-4-turbo',
        n=1,
        response_format=components.ResponseFormat(
            type=components.CreateChatCompletionRequestType.JSON_OBJECT,
        ),
        temperature=1,
        top_p=1,
        user='user-1234',
    ),
    response=components.CreateChatCompletionResponse(
        id='<id>',
        choices=[
            components.Choices(
                finish_reason=components.FinishReason.CONTENT_FILTER,
                index=859213,
                message=components.ChatCompletionResponseMessage(
                    content='<value>',
                    role=components.ChatCompletionRole.ASSISTANT,
                ),
                logprobs=components.Logprobs(
                    content=[
                        components.ChatCompletionTokenLogprob(
                            token='<value>',
                            logprob=2884.08,
                            bytes=[
                                134365,
                            ],
                            top_logprobs=[
                                components.TopLogprobs(
                                    token='<value>',
                                    logprob=7865.46,
                                    bytes=[
                                        69025,
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
            ),
        ],
        created=996706,
        model='gpt-4-turbo',
        object=components.Object.CHAT_COMPLETION,
    ),
), x_log10_organization='<value>')

if res.any is not None:
    # handle response
    pass

```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import log10
from log10.models import components

s = log10.Log10(
    server_url="https://log10.io",
    log10_token="<YOUR_API_KEY_HERE>",
)


res = s.completions.create(completion=components.Completion(
    organization_id='<value>',
    request=components.CreateChatCompletionRequest(
        messages=[
            components.ChatCompletionRequestAssistantMessage(
                role=components.ChatCompletionRole.ASSISTANT,
            ),
        ],
        model='gpt-4-turbo',
        n=1,
        response_format=components.ResponseFormat(
            type=components.CreateChatCompletionRequestType.JSON_OBJECT,
        ),
        temperature=1,
        top_p=1,
        user='user-1234',
    ),
    response=components.CreateChatCompletionResponse(
        id='<id>',
        choices=[
            components.Choices(
                finish_reason=components.FinishReason.CONTENT_FILTER,
                index=859213,
                message=components.ChatCompletionResponseMessage(
                    content='<value>',
                    role=components.ChatCompletionRole.ASSISTANT,
                ),
                logprobs=components.Logprobs(
                    content=[
                        components.ChatCompletionTokenLogprob(
                            token='<value>',
                            logprob=2884.08,
                            bytes=[
                                134365,
                            ],
                            top_logprobs=[
                                components.TopLogprobs(
                                    token='<value>',
                                    logprob=7865.46,
                                    bytes=[
                                        69025,
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
            ),
        ],
        created=996706,
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

| Name          | Type          | Scheme        |
| ------------- | ------------- | ------------- |
| `log10_token` | apiKey        | API key       |

To authenticate with the API the `log10_token` parameter must be set when initializing the SDK client instance. For example:
```python
import log10
from log10.models import components

s = log10.Log10(
    log10_token="<YOUR_API_KEY_HERE>",
)


res = s.completions.create(completion=components.Completion(
    organization_id='<value>',
    request=components.CreateChatCompletionRequest(
        messages=[
            components.ChatCompletionRequestAssistantMessage(
                role=components.ChatCompletionRole.ASSISTANT,
            ),
        ],
        model='gpt-4-turbo',
        n=1,
        response_format=components.ResponseFormat(
            type=components.CreateChatCompletionRequestType.JSON_OBJECT,
        ),
        temperature=1,
        top_p=1,
        user='user-1234',
    ),
    response=components.CreateChatCompletionResponse(
        id='<id>',
        choices=[
            components.Choices(
                finish_reason=components.FinishReason.CONTENT_FILTER,
                index=859213,
                message=components.ChatCompletionResponseMessage(
                    content='<value>',
                    role=components.ChatCompletionRole.ASSISTANT,
                ),
                logprobs=components.Logprobs(
                    content=[
                        components.ChatCompletionTokenLogprob(
                            token='<value>',
                            logprob=2884.08,
                            bytes=[
                                134365,
                            ],
                            top_logprobs=[
                                components.TopLogprobs(
                                    token='<value>',
                                    logprob=7865.46,
                                    bytes=[
                                        69025,
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
            ),
        ],
        created=996706,
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
