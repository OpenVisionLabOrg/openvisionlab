from openvisionlab.core.registry import Registry


def test_register_component() -> None:
    registry = Registry[type]("models")

    class Dummy:
        pass

    registry.register(Dummy)
