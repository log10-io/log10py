# ChatCompletionRequestToolMessage


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `role`                                                                         | [components.ChatCompletionRole](../../models/components/chatcompletionrole.md) | :heavy_check_mark:                                                             | The role of the author of a message                                            |
| `content`                                                                      | *str*                                                                          | :heavy_check_mark:                                                             | The contents of the tool message.                                              |
| `tool_call_id`                                                                 | *str*                                                                          | :heavy_check_mark:                                                             | Tool call that this message is responding to.                                  |