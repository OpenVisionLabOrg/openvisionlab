from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class ModelMetadata:
    """Metadata describing a model."""

    name: str
    task: str
    framework: str
    version: str
