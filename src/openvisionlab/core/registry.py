from __future__ import annotations

from collections.abc import Callable
from typing import Generic, TypeVar, overload

from openvisionlab.core.exceptions import DuplicateRegistrationError

T = TypeVar("T")


class Registry(Generic[T]):
    """A generic registry for OpenVisionLab components."""

    def __init__(self, name: str) -> None:
        self._name = name
        self._items: dict[str, T] = {}

    @overload
    def register(self, obj: T) -> T: ...

    @overload
    def register(self, name: str) -> Callable[[T], T]: ...

    @overload
    def register(self) -> Callable[[T], T]: ...

    def register(
        self,
        obj: T | str | None = None,
        *,
        name: str | None = None,
    ) -> T | Callable[[T], T]:
        if obj is None or isinstance(obj, str):
            alias = obj

            def decorator(component: T) -> T:
                self._register(component, alias or name)
                return component

            return decorator
        self._register(obj, name)
        return obj

    def _register(
        self,
        component: T,
        name: str | None,
    ) -> None:
        key = name or component.__name__
        if key in self._items:
            raise DuplicateRegistrationError(
                f"Component '{key}' is already registered in registry '{self._name}'."
            )
        self._items[key] = component
