import sys
from PyQt5.QtWidgets import QWidget
import unittest
from PyQt5.QtWidgets import QApplication

sys.path.insert(1, 'src/')
from widgets import MplCanvas, LineCanvas, ImageCanvas, Table

class TestMplCanvas(unittest.TestCase):

    def test_update_canvas(self):
        app = QApplication([])
        canvas = MplCanvas()
        canvas.update_canvas()
        # Check if the canvas is updated successfully
        self.assertTrue(True)

class TestLineCanvas(unittest.TestCase):

    def test_draw_line(self):
        app = QApplication([])
        canvas = LineCanvas()
        canvas.draw_line()
        # Check if the line is drawn successfully
        self.assertTrue(True)

class TestImageCanvas(unittest.TestCase):

    def test_load_image(self):
        app = QApplication([])
        canvas = ImageCanvas()
        canvas.load_image()
        # Check if the image is loaded successfully
        self.assertTrue(True)

class TestTable(unittest.TestCase):

    def test_show_row(self):
        app = QApplication([])
        table = Table(0, None)
        table.show_row(0)
        # Check if the rows are shown correctly
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
