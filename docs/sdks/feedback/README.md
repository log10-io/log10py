# Feedback
(*feedback*)

## Overview

Feedback

### Available Operations

* [get](#get) - Fetch feedback by id.
* [list](#list) - List feedback
* [upload](#upload) - Upload a piece of feedback

## get

Fetch feedback by id.

### Example Usage

```python
import log10

s = log10.Log10(
    log10_token='<YOUR_API_KEY_HERE>',
)


res = s.feedback.get(feedback_id='<id>', x_log10_organization='<value>')

if res.feedback is not None:
    # handle response
    pass

```

### Parameters

| Parameter                 | Type                      | Required                  | Description               |
| ------------------------- | ------------------------- | ------------------------- | ------------------------- |
| `feedback_id`             | *str*                     | :heavy_check_mark:        | The feedback id to fetch. |
| `x_log10_organization`    | *Optional[str]*           | :heavy_minus_sign:        | N/A                       |

### Response

**[operations.GetResponse](../../models/operations/getresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list

List feedback

### Example Usage

```python
import log10

s = log10.Log10(
    log10_token='<YOUR_API_KEY_HERE>',
)


res = s.feedback.list(x_log10_organization='<value>')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `x_log10_organization`                                                             | *Optional[str]*                                                                    | :heavy_minus_sign:                                                                 | N/A                                                                                |
| `request_body`                                                                     | [Optional[operations.ListRequestBody]](../../models/operations/listrequestbody.md) | :heavy_minus_sign:                                                                 | N/A                                                                                |

### Response

**[operations.ListResponse](../../models/operations/listresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## upload

Upload a piece of feedback

### Example Usage

```python
import log10
from log10.models import operations

s = log10.Log10(
    log10_token='<YOUR_API_KEY_HERE>',
)


res = s.feedback.upload(request_body=operations.One(
    organization_id='<id>',
    task_id='<id>',
    json_values=operations.JSONValues(),
    matched_completion_ids=[
        '<value>',
        '<value>',
    ],
    comment='The Apollotech B340 is an affordable wireless mouse with reliable connectivity, 12 months battery life and modern design',
    completion_tags_selector=[
        '<value>',
    ],
    allow_unmatched_feedback=False,
    max_matched_completions=100,
), x_log10_organization='<value>')

if res.feedback is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request_body`                                                               | [operations.UploadRequestBody](../../models/operations/uploadrequestbody.md) | :heavy_check_mark:                                                           | N/A                                                                          |
| `x_log10_organization`                                                       | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | N/A                                                                          |

### Response

**[operations.UploadResponse](../../models/operations/uploadresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |