# RFC 0001

## Title

Generic Registry

## Status

Accepted

## Motivation

OpenVisionLab requires a generic registry that allows components such as models,
plugins, exporters and pipelines to be registered dynamically while keeping the
core framework extensible.

## Decision

A generic registry will be implemented inside `openvisionlab.core`.

Every future component registration should rely on this system.

## Consequences

- Consistent architecture
- Plugin-friendly
- Easier extension
- Centralized component discovery