# ~~ChatCompletionRequestFunctionMessage~~

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `role`                                                                         | [components.ChatCompletionRole](../../models/components/chatcompletionrole.md) | :heavy_check_mark:                                                             | The role of the author of a message                                            |
| `content`                                                                      | *Optional[str]*                                                                | :heavy_check_mark:                                                             | The contents of the function message.                                          |
| `name`                                                                         | *str*                                                                          | :heavy_check_mark:                                                             | The name of the function to call.                                              |