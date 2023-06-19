import sys
from PyQt5.QtWidgets import QWidget
import unittest
from PyQt5.QtWidgets import QApplication

sys.path.insert(1, 'src/')
from widgets import MplCanvas, LineCanvas, ImageCanvas, Table

from matplotlib.figure import Figure
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg


class TestCanvas(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])
        self.canvas = MplCanvas()

    def test_canvas_initialization(self):
        self.assertIsInstance(self.canvas.fig, Figure)
        self.assertIsInstance(self.canvas, FigureCanvasQTAgg)
        self.assertIsNotNone(self.canvas.axes)

    def test_update_canvas(self):
        self.canvas.update_canvas()
        # Assert that the canvas was updated successfully

class TestLineCanvas(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])
        self.det_ = 0  
        self.canvas = LineCanvas(self.det_)

    def test_draw_line(self):
        self.canvas.draw_line()
        # Assert that the line was drawn successfully

class TestImageCanvas(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])
        self.det_ = 0 
        self.canvas = ImageCanvas(self.det_)

    def test_load_image(self):
        self.canvas.load_image()
        # Assert that the image was loaded successfully

    def test_draw_next_image(self):
        self.canvas.draw_next_image()
        # Assert that the next image was loaded successfully

    def test_draw_previous_image(self):
        self.canvas.draw_previous_image()
        # Assert that the previous image was loaded successfully

    def test_update_image_from_slider(self):
        value = 50  # Replace with your own test value
        self.canvas.update_image_from_slider(value)
        # Assert that the image was updated successfully

class TestTable(unittest.TestCase):
    def setUp(self):
        self.current_image_idx = 0  # Replace with your own test value
        self.det = 0  
        self.table = Table(self.current_image_idx, self.det)

    def test_show_row(self):
        self.table.show_row(self.current_image_idx)
        # Assert that the correct rows were shown in the table

    def test_numbers_of_rows(self):
        row_indices = self.table.numbers_of_rows()
        # Assert that the correct row indices were returned

if __name__ == '__main__':
    unittest.main()
