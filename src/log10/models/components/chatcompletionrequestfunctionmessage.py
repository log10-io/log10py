"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .chatcompletionrole import ChatCompletionRole
from dataclasses_json import Undefined, dataclass_json
from log10 import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ChatCompletionRequestFunctionMessage:
    r"""Deprecated class: This will be removed in a future release, please migrate away from it as soon as possible."""
    role: ChatCompletionRole = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('role') }})
    r"""The role of the author of a message"""
    content: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('content') }})
    r"""The contents of the function message."""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The name of the function to call."""
    

