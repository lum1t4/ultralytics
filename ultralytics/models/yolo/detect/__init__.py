# Ultralytics YOLO 🚀, AGPL-3.0 license

from .predict import DetectionPredictor
from .train import DetectionTrainer, MultiChannelDetectionTrainer
from .val import DetectionValidator

__all__ = "DetectionPredictor", "DetectionTrainer", "DetectionValidator", "MultiChannelDetectionTrainer"
