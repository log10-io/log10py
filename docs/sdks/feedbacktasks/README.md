# FeedbackTasks
(*feedback_tasks*)

## Overview

FeedbackTasks

### Available Operations

* [list](#list) - List feedback tasks.
* [create](#create) - Create a new task.
* [get](#get) - Retrieves feedback task `taskId`.

## list

List feedback tasks.

### Example Usage

```python
import log10

s = log10.Log10(
    log10_token="<YOUR_API_KEY_HERE>",
)


res = s.feedback_tasks.list()

if res.tasks is not None:
    # handle response
    pass

```


### Response

**[operations.ListFeedbackTasksResponse](../../models/operations/listfeedbacktasksresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## create

Create a new task.

### Example Usage

```python
import log10
from log10.models import components

s = log10.Log10(
    log10_token="<YOUR_API_KEY_HERE>",
)


res = s.feedback_tasks.create(request=components.Task(
    json_schema=components.JSONSchema(),
    name='<value>',
    instruction='<value>',
    completion_tags_selector=components.CompletionTagsSelector(),
))

if res.task is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                          | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `request`                                          | [components.Task](../../models/components/task.md) | :heavy_check_mark:                                 | The request object to use for the request.         |


### Response

**[operations.CreateFeedbackTaskResponse](../../models/operations/createfeedbacktaskresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get

Retrieves feedback task `taskId`.

### Example Usage

```python
import log10

s = log10.Log10(
    log10_token="<YOUR_API_KEY_HERE>",
)


res = s.feedback_tasks.get(task_id='<value>')

if res.task is not None:
    # handle response
    pass

```

### Parameters

| Parameter             | Type                  | Required              | Description           |
| --------------------- | --------------------- | --------------------- | --------------------- |
| `task_id`             | *str*                 | :heavy_check_mark:    | The task id to fetch. |


### Response

**[operations.GetFeedbackTaskResponse](../../models/operations/getfeedbacktaskresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
