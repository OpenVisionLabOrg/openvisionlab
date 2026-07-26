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


class Dummy:
    pass


def test_contains_registered_component() -> None:
    registry = Registry[type]("models")

    registry.register(Dummy)

    assert "Dummy" in registry


def test_contains_unknown_component() -> None:
    registry = Registry[type]("models")

    assert "Unknown" not in registry


def test_registry_length() -> None:
    registry = Registry[type]("models")

    class Dummy:
        pass

    registry.register(Dummy)

    assert len(registry) == 1


def test_registry_iteration() -> None:
    registry = Registry[type]("models")

    class Dummy:
        pass

    registry.register(Dummy)

    assert list(registry) == [Dummy]


def test_registry_getitem() -> None:
    registry = Registry[type]("models")

    class Dummy:
        pass

    registry.register(Dummy)

    assert registry["Dummy"] is Dummy
