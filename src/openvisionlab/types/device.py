from __future__ import annotations

from enum import StrEnum


class Device(StrEnum):
    """Supported execution devices."""

    CPU = "cpu"
    CUDA = "cuda"
    MPS = "mps"
