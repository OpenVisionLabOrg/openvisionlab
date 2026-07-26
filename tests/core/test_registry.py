import pytest

from openvisionlab.core.exceptions import ComponentNotFoundError
from openvisionlab.core.registry import Registry


def test_register_component() -> None:
    registry = Registry[type]("models")

    class Dummy:
        pass

    registry.register(Dummy)


def test_get_registered_component() -> None:
    registry = Registry[type]("models")

    class Dummy:
        pass

    registry.register(Dummy)

    assert registry.get("Dummy") is Dummy


def test_get_unknown_component() -> None:
    registry = Registry[type]("models")

    with pytest.raises(ComponentNotFoundError):
        registry.get("Unknown")
