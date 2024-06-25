# Sessions
(*sessions*)

## Overview

Sessions

### Available Operations

* [create](#create) - Create a session

## create

Create a session

### Example Usage

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

### Parameters

| Parameter              | Type                   | Required               | Description            |
| ---------------------- | ---------------------- | ---------------------- | ---------------------- |
| `x_log10_organization` | *Optional[str]*        | :heavy_minus_sign:     | N/A                    |


### Response

**[operations.CreateSessionResponse](../../models/operations/createsessionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
