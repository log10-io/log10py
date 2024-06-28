"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import feedback as components_feedback
from ...models.components import httpmetadata as components_httpmetadata
from dataclasses_json import Undefined, dataclass_json
from log10 import utils
from typing import List, Optional, Union


@dataclasses.dataclass
class UploadGlobals:
    x_log10_organization: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'X-Log10-Organization', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class RequestBodyJSONValues:
    r"""The values of the feedback. Must be valid JSON according to the task schema."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Two:
    organization_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('organization_id') }})
    r"""The unique identifier for the organization."""
    task_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('task_id') }})
    r"""The unique identifier for the task associated with this feedback."""
    json_values: RequestBodyJSONValues = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('json_values') }})
    r"""The values of the feedback. Must be valid JSON according to the task schema."""
    matched_completion_ids: List[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('matched_completion_ids') }})
    r"""The matched completion ids associated with this feedback."""
    comment: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('comment') }})
    r"""The comment associated with this feedback."""
    completion_ids: List[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('completion_ids') }})
    r"""The completion ids to associate with this feedback."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""The unique identifier for this feedback."""
    created_at_ms: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at_ms'), 'exclude': lambda f: f is None }})
    r"""The epoch this schema was created."""
    completions_summary: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('completions_summary'), 'exclude': lambda f: f is None }})
    



@dataclasses.dataclass
class JSONValues:
    r"""The values of the feedback. Must be valid JSON according to the task schema."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class One:
    organization_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('organization_id') }})
    r"""The unique identifier for the organization."""
    task_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('task_id') }})
    r"""The unique identifier for the task associated with this feedback."""
    json_values: JSONValues = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('json_values') }})
    r"""The values of the feedback. Must be valid JSON according to the task schema."""
    matched_completion_ids: List[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('matched_completion_ids') }})
    r"""The matched completion ids associated with this feedback."""
    comment: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('comment') }})
    r"""The comment associated with this feedback."""
    completion_tags_selector: List[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('completion_tags_selector') }})
    r"""The completion tags associated with this feedback."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""The unique identifier for this feedback."""
    created_at_ms: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at_ms'), 'exclude': lambda f: f is None }})
    r"""The epoch this schema was created."""
    completions_summary: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('completions_summary'), 'exclude': lambda f: f is None }})
    allow_unmatched_feedback: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('allow_unmatched_feedback'), 'exclude': lambda f: f is None }})
    r"""Whether to allow unmatched feedback. Defaults to false."""
    max_matched_completions: Optional[int] = dataclasses.field(default=100, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('max_matched_completions'), 'exclude': lambda f: f is None }})
    r"""The maximum number of matched completions. Returns error if exceeded. Defaults to 100."""
    



@dataclasses.dataclass
class UploadRequest:
    request_body: UploadRequestBody = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    x_log10_organization: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'X-Log10-Organization', 'style': 'simple', 'explode': False }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UploadResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field(metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    feedback: Optional[components_feedback.Feedback] = dataclasses.field(default=None)
    r"""OK"""
    


UploadRequestBody = Union[One, Two]
