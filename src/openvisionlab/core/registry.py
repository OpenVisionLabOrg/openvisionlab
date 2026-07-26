from __future__ import annotations

from typing import Generic, TypeVar

T = TypeVar("T")


class Registry(Generic[T]):
    """A generic registry for OpenVisionLab components."""

    def __init__(self, name: str) -> None:
        self._name = name
        self._items: dict[str, T] = {}