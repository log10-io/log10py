"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .chatcompletionrequestmessagecontentpart import ChatCompletionRequestMessageContentPart
from .chatcompletionrole import ChatCompletionRole
from dataclasses_json import Undefined, dataclass_json
from log10 import utils
from typing import List, Optional, Union


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ChatCompletionRequestUserMessage:
    content: Content = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('content') }})
    r"""The contents of the user message."""
    role: ChatCompletionRole = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('role') }})
    r"""The role of the author of a message"""
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""An optional name for the participant. Provides the model information to differentiate between participants of the same role."""
    


Content = Union[str, List[ChatCompletionRequestMessageContentPart]]
