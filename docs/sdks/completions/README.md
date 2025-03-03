# Completions
(*completions*)

## Overview

Completions

### Available Operations

* [create](#create) - Create a completion
* [update](#update) - Update completion by id.
* [list_ungraded](#list_ungraded) - List ungraded completions i.e. completions that have not been associated with feedback but matches task selector.

## create

Create a completion

### Example Usage

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

### Parameters

| Parameter                                                      | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `completion`                                                   | [components.Completion](../../models/components/completion.md) | :heavy_check_mark:                                             | N/A                                                            |
| `x_log10_organization`                                         | *Optional[str]*                                                | :heavy_minus_sign:                                             | N/A                                                            |

### Response

**[operations.CreateResponse](../../models/operations/createresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update

Update completion by id.

### Example Usage

```python
import log10
from log10.models import components

s = log10.Log10(
    log10_token='<YOUR_API_KEY_HERE>',
)


res = s.completions.update(completion=components.Completion(
    organization_id='<id>',
    request=components.CreateChatCompletionRequest(
        messages=[
            components.ChatCompletionRequestAssistantMessage(
                role=components.ChatCompletionRole.USER,
            ),
            components.ChatCompletionRequestAssistantMessage(
                role=components.ChatCompletionRole.TOOL,
                content='<value>',
                name='<value>',
            ),
            components.ChatCompletionRequestAssistantMessage(
                role=components.ChatCompletionRole.FUNCTION,
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
        created=896501,
        model='gpt-4-turbo',
        object=components.Object.CHAT_COMPLETION,
    ),
), completion_id='<id>', x_log10_organization='<value>')

if res.completion is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                      | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `completion_id`                                                | *str*                                                          | :heavy_check_mark:                                             | The completion id to update.                                   |
| `completion`                                                   | [components.Completion](../../models/components/completion.md) | :heavy_check_mark:                                             | N/A                                                            |
| `x_log10_organization`                                         | *Optional[str]*                                                | :heavy_minus_sign:                                             | N/A                                                            |

### Response

**[operations.UpdateResponse](../../models/operations/updateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_ungraded

List ungraded completions i.e. completions that have not been associated with feedback but matches task selector.

### Example Usage

```python
import log10

s = log10.Log10(
    log10_token='<YOUR_API_KEY_HERE>',
)


res = s.completions.list_ungraded(x_log10_organization='<value>')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter              | Type                   | Required               | Description            |
| ---------------------- | ---------------------- | ---------------------- | ---------------------- |
| `x_log10_organization` | *Optional[str]*        | :heavy_minus_sign:     | N/A                    |

### Response

**[operations.ListUngradedResponse](../../models/operations/listungradedresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |