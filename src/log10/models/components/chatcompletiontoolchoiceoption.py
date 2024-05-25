"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from .chatcompletionnamedtoolchoice import ChatCompletionNamedToolChoice
from enum import Enum
from typing import Union


class ChatCompletionToolChoiceOption1(str, Enum):
    r"""`none` means the model will not call any tool and instead generates a message. `auto` means the model can pick between generating a message or calling one or more tools. `required` means the model must call one or more tools."""
    NONE = 'none'
    AUTO = 'auto'
    REQUIRED = 'required'

ChatCompletionToolChoiceOption = Union['ChatCompletionToolChoiceOption1', ChatCompletionNamedToolChoice]