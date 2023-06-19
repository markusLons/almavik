import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
import unittest
from unittest.mock import MagicMock
sys.path.insert(1, 'src/')
from widgets import MplCanvas, LineCanvas, ImageCanvas, Table
import os
os.environ['DISPLAY'] = ':0'
from PyQt5.QtWidgets import QTableWidgetItem



class TestMplCanvas(unittest.TestCase):

    def test_update_canvas(self):
        canvas = MplCanvas()
        canvas.fig.canvas.draw = MagicMock()

        canvas.update_canvas()

        canvas.fig.canvas.draw.assert_called_once()


class TestLineCanvas(unittest.TestCase):

    def test_draw_line(self):
        det_mock = MagicMock()
        det_mock.center_mass = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        canvas = LineCanvas(det_=det_mock, current_image_idx=1)
        canvas.axes.clear = MagicMock()
        canvas.update_canvas = MagicMock()

        canvas.draw_line()

        canvas.axes.clear.assert_called_once()
        canvas.update_canvas.assert_called_once()


class TestImageCanvas(unittest.TestCase):

    def test_load_image(self):
        det_mock = MagicMock()
        det_mock.img = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        canvas = ImageCanvas(det_=det_mock)
        canvas.load_image()

        self.assertIsNotNone(canvas.img)
        self.assertEqual(canvas.img.get_array().tolist(), det_mock.img)

    def test_draw_next_image(self):
        det_mock = MagicMock()
        det_mock.img = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        canvas = ImageCanvas(det_=det_mock)
        canvas.load_image = MagicMock()

        canvas.draw_next_image()

        canvas.load_image.assert_called_once()

    def test_draw_previous_image(self):
        det_mock = MagicMock()
        det_mock.img = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        canvas = ImageCanvas(det_=det_mock)
        canvas.load_image = MagicMock()

        canvas.draw_previous_image()

        canvas.load_image.assert_called_once()

    def test_update_image_from_slider(self):
        det_mock = MagicMock()
        det_mock.img = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        canvas = ImageCanvas(det_=det_mock)
        canvas.load_image = MagicMock()

        canvas.update_image_from_slider(50)

        canvas.load_image.assert_called_once()


class TestTable(unittest.TestCase):

    def test_show_row(self):
        det_mock = MagicMock()
        det_mock.center_mass = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        table = Table(current_image_idx=1, det=det_mock)
        table.table.setItem = MagicMock()

        table.show_row(1)

        calls = [MagicMock(), MagicMock(), MagicMock()]
        calls[0].assert_called_with(0, 0, QTableWidgetItem("4"))
        calls[1].assert_called_with(0, 1, QTableWidgetItem("5"))
        calls[2].assert_called_with(0, 2, QTableWidgetItem("6"))


if __name__ == '__main__':
    unittest.main()
