"""Custom exceptions for OpenVisionLab."""

from __future__ import annotations


class OpenVisionLabError(Exception):
    """Base exception for all OpenVisionLab errors."""


class RegistryError(OpenVisionLabError):
    """Base exception for registry-related errors."""


class DuplicateRegistrationError(RegistryError):
    """Raised when attempting to register an existing key."""


class ComponentNotFoundError(RegistryError):
    """Raised when a requested component does not exist."""