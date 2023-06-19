import sys
from PyQt5.QtWidgets import QWidget
import unittest
from PyQt5.QtWidgets import QApplication
from unittest.mock import MagicMock
sys.path.insert(1, 'src/')
from widgets import MplCanvas, LineCanvas, ImageCanvas, Table
import os
os.environ['DISPLAY'] = ':0'


class TestImageCanvas(unittest.TestCase):
    def test_load_image(self):
        # Создаем экземпляр ImageCanvas
        canvas = ImageCanvas()

        # Задаем тестовые данные
        canvas.img_without_contour = [MagicMock()]
        canvas.img_with_contour = [MagicMock()]
        canvas.current_image_idx = 0
        canvas.contour_or_not = 0

        # Вызываем метод load_image()
        canvas.load_image()

        # Проверяем, что изображение было успешно загружено
        self.assertIsNotNone(canvas.img)


if __name__ == '__main__':
    unittest.main()
