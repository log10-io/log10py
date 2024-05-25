"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import completion as components_completion
from ...models.components import httpmetadata as components_httpmetadata
from dataclasses_json import Undefined, dataclass_json
from typing import Any, Optional


@dataclasses.dataclass
class CreateGlobals:
    x_log10_organization: str = dataclasses.field(metadata={'header': { 'field_name': 'X-Log10-Organization', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class CreateRequest:
    completion: components_completion.Completion = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    x_log10_organization: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'X-Log10-Organization', 'style': 'simple', 'explode': False }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field(metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    any: Optional[Any] = dataclasses.field(default=None)
    r"""Created"""
    completion: Optional[components_completion.Completion] = dataclasses.field(default=None)
    r"""Created"""
    
