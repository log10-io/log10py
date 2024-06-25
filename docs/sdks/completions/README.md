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
    log10_token="<YOUR_API_KEY_HERE>",
)


res = s.completions.create(completion=components.Completion(
    organization_id='<value>',
    request=components.CreateChatCompletionRequest(
        messages=[
            components.ChatCompletionRequestAssistantMessage(
                role=components.ChatCompletionRequestAssistantMessageRole.ASSISTANT,
            ),
        ],
        model=components.Two.GPT_4_TURBO,
        n=1,
        response_format=components.ResponseFormat(
            type=components.CreateChatCompletionRequestType.JSON_OBJECT,
        ),
        temperature=1,
        top_p=1,
        user='user-1234',
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

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## update

Update completion by id.

### Example Usage

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
                role=components.ChatCompletionRequestFunctionMessageRole.FUNCTION,
                content='<value>',
                name='<value>',
            ),
        ],
        model=components.Two.GPT_4_TURBO,
        n=1,
        response_format=components.ResponseFormat(
            type=components.CreateChatCompletionRequestType.JSON_OBJECT,
        ),
        temperature=1,
        top_p=1,
        user='user-1234',
    ),
), x_log10_organization='<value>')

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

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## list_ungraded

List ungraded completions i.e. completions that have not been associated with feedback but matches task selector.

### Example Usage

```python
import log10

s = log10.Log10(
    log10_token="<YOUR_API_KEY_HERE>",
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

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
