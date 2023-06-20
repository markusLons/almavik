import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
import unittest
from unittest.mock import patch
import os

sys.path.insert(1, 'src/')
from YPPRPO import Window, detectorDrop

# Получаем текущую директорию (папку, в которой находится этот файл)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Путь к папке с изображениями относительно корневой папки проекта
img_dir = os.path.join(current_dir, '../../exp1')

class WindowTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = QApplication(sys.argv)

    @patch("YPPRPO.ImageCanvas")
    def test_previous_image_button(self, mock_image_canvas):
        det = detectorDrop(img_dir)
        window = Window(det)
        window.slider.setValue(1)  # Set slider value to 1
        mock_image_canvas.current_image_idx = 1
        window.button1_clicked()  # Call the function associated with the previous image button
        self.assertEqual(mock_image_canvas.draw_previous_image.call_count, 1)
        self.assertEqual(mock_image_canvas.current_image_idx, 0)
        self.assertEqual(window.table.current_row, 0)
        self.assertEqual(window.slider.value(), 0)

    @patch("YPPRPO.ImageCanvas")
    def test_next_image_button(self, mock_image_canvas):
        det = detectorDrop(img_dir)
        window = Window(det)
        window.slider.setValue(1)  # Set slider value to 1
        mock_image_canvas.current_image_idx = 1
        window.button2_clicked()  # Call the function associated with the next image button
        self.assertEqual(mock_image_canvas.draw_next_image.call_count, 1)
        self.assertEqual(mock_image_canvas.current_image_idx, 2)
        self.assertEqual(window.table.current_row, 2)
        self.assertEqual(window.slider.value(), 2)

    @patch("YPPRPO.ImageCanvas")
    def test_toggle_contour_mode_button(self, mock_image_canvas):
        det = detectorDrop(img_dir)
        window = Window(det)
        window.button3_clicked()  # Call the function associated with the toggle contour mode button
        self.assertEqual(mock_image_canvas.contour_or_not, 1)
        self.assertEqual(window.button3.text(), "Disable Drop Contour Mode")
        window.button3_clicked()  # Call the function again to disable contour mode
        self.assertEqual(mock_image_canvas.contour_or_not, 0)
        self.assertEqual(window.button3.text(), "Enable Drop Contour Mode")

def run_tests():
    unittest.main()

if __name__ == '__main__':
    run_tests()
