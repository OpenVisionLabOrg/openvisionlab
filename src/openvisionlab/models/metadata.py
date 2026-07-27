from __future__ import annotations

from dataclasses import dataclass

from openvisionlab.types import Task


@dataclass(slots=True, frozen=True)
class ModelMetadata:
    """Metadata describing a model."""

    name: str
    task: Task
    framework: str
    version: str
