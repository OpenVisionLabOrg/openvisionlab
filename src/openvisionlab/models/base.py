from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any

from openvisionlab.types import Device

from .metadata import ModelMetadata


class BaseModel(ABC):
    """Abstract base class for all OpenVisionLab models."""

    def __init__(
        self,
        *,
        metadata: ModelMetadata,
        weights: str | Path | None = None,
        device: Device = Device.CPU,
    ) -> None:
        self._metadata = metadata
        self._weights = Path(weights) if weights is not None else None
        self._device = device

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, device={self.device.value!r})"

    @property
    def name(self) -> str:
        """Return the model name."""
        return self._metadata.name

    @property
    def weights(self) -> Path | None:
        """Return the model weights path."""
        return self._weights

    @property
    def task(self) -> str:
        return self._metadata.task

    @property
    def framework(self) -> str:
        return self._metadata.framework

    @property
    def version(self) -> str:
        return self._metadata.version

    @property
    def device(self) -> Device:
        """Return the execution device."""
        return self._device

    @property
    def metadata(self) -> ModelMetadata:
        """Return the model metadata."""
        return self._metadata

    @abstractmethod
    def predict(self, *args: Any, **kwargs: Any) -> Any:
        """Run inference."""
        raise NotImplementedError
