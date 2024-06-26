"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from log10 import utils
from typing import Optional


@dataclasses.dataclass
class JSONSchema:
    r"""The schema of the task. Must be valid JSON Schema."""
    



@dataclasses.dataclass
class CompletionTagsSelector:
    r"""The completion tag matching with this task i.e. surfaced as needing feedback."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Task:
    json_schema: JSONSchema = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('json_schema') }})
    r"""The schema of the task. Must be valid JSON Schema."""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The name of the task."""
    instruction: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('instruction') }})
    r"""The instructions for this task."""
    completion_tags_selector: CompletionTagsSelector = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('completion_tags_selector') }})
    r"""The completion tag matching with this task i.e. surfaced as needing feedback."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""The unique identifier for this task."""
    created_at_ms: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at_ms'), 'exclude': lambda f: f is None }})
    r"""The epoch this schema was created."""
    

