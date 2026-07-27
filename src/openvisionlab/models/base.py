from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path


class BaseModel(ABC):
    """Abstract base class for all OpenVisionLab models."""

    def __init__(
        self,
        *,
        name: str,
        weights: str | Path | None = None,
    ) -> None:
        self._name = name
        self._weights = Path(weights) if weights is not None else None

    @property
    def name(self) -> str:
        """Return the model name."""
        return self._name

    @property
    def weights(self) -> Path | None:
        """Return the model weights path."""
        return self._weights

    @abstractmethod
    def predict(self, *args: Any, **kwargs: Any) -> Any:
        """Run inference."""
        raise NotImplementedError
