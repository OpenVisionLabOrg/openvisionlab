from __future__ import annotations

from openvisionlab.core.registry import Registry

from .base import BaseModel

MODELS = Registry[type[BaseModel]]("models")
