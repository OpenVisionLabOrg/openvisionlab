from __future__ import annotations

from enum import StrEnum


class Task(StrEnum):
    """Supported computer vision tasks."""

    CLASSIFICATION = "classification"
    DETECTION = "detection"
    SEGMENTATION = "segmentation"
    INSTANCE_SEGMENTATION = "instance_segmentation"
    POSE_ESTIMATION = "pose_estimation"
    TRACKING = "tracking"
    OCR = "ocr"
    DEPTH_ESTIMATION = "depth_estimation"
