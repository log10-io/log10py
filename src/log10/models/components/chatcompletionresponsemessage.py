"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .chatcompletionmessagetoolcall import ChatCompletionMessageToolCall
from .chatcompletionrole import ChatCompletionRole
from dataclasses_json import Undefined, dataclass_json
from log10 import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ChatCompletionResponseMessageFunctionCall:
    r"""Deprecated and replaced by `tool_calls`. The name and arguments of a function that should be called, as generated by the model.

    Deprecated class: This will be removed in a future release, please migrate away from it as soon as possible.
    """
    arguments: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('arguments') }})
    r"""The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function."""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The name of the function to call."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ChatCompletionResponseMessage:
    r"""A chat completion message generated by the model."""
    content: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('content') }})
    r"""The contents of the message."""
    role: ChatCompletionRole = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('role') }})
    r"""The role of the author of a message"""
    tool_calls: Optional[List[ChatCompletionMessageToolCall]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tool_calls'), 'exclude': lambda f: f is None }})
    r"""The tool calls generated by the model, such as function calls."""
    function_call: Optional[ChatCompletionResponseMessageFunctionCall] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('function_call'), 'exclude': lambda f: f is None }})
    r"""Deprecated and replaced by `tool_calls`. The name and arguments of a function that should be called, as generated by the model.

    Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible.
    """
    

