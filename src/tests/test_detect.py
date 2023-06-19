import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
import unittest
sys.path.insert(1, 'src/')
from detectorDrop import detectorDrop

img_dir = os.path.abspath('exp1')

class TestDetectorDrop(unittest.TestCase):

    def setUp(self):
        # Создаем экземпляр класса detectorDrop
        self.detector = detectorDrop(img_dir)

    def test_center_mass(self):
        # Проверяем, что center_mass является списком
        self.assertIsInstance(self.detector.center_mass, list)

    def test_img(self):
        # Проверяем, что img является списком
        self.assertIsInstance(self.detector.img, list)

    def test_img_contour(self):
        # Проверяем, что img_contour является списком
        self.assertIsInstance(self.detector.img_contour, list)

    def test_shaded_contours(self):
        # Создаем фиктивное изображение для тестирования
        image = np.zeros((100, 100, 3), dtype=np.uint8)
        result = self.detector.shaded_contours(image)
        # Проверяем, что результат имеет тот же размер, что и исходное изображение
        self.assertEqual(result.shape, image.shape)

    def test_init(self):
        # Проверяем, что после инициализации экземпляра класса, все списки имеют одинаковую длину
        self.assertEqual(len(self.detector.center_mass), len(self.detector.img))
        self.assertEqual(len(self.detector.center_mass), len(self.detector.img_contour))

        # Проверяем, что каждый элемент списка center_mass является кортежем с тремя значениями
        for item in self.detector.center_mass:
            self.assertIsInstance(item, tuple)
            self.assertEqual(len(item), 3)

        # Проверяем, что каждый элемент списка img является изображением numpy array
        for img in self.detector.img:
            self.assertIsInstance(img, np.ndarray)
            self.assertEqual(img.ndim, 3)  # Проверяем, что изображение имеет 3 канала (BGR)

        # Проверяем, что каждый элемент списка img_contour является изображением numpy array
        for img_contour in self.detector.img_contour:
            self.assertIsInstance(img_contour, np.ndarray)
            self.assertEqual(img_contour.ndim, 3)  # Проверяем, что изображение имеет 3 канала (BGR)

if __name__ == '__main__':
    unittest.main()
