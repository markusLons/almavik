import pytest
from ..src.detectorDrop import detectorDrop

def test_detectorDrop_lists_length():
    images_folder = "./exp1"

    detector = detectorDrop(images_folder)

    assert len(detector.center_mass) == len(detector.img) == len(detector.img_contour) == 0
