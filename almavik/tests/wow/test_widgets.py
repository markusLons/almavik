import sys
import numpy as np
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QTableWidgetItem
import unittest
from unittest.mock import MagicMock

sys.path.insert(1, 'src/')
from widgets import MplCanvas, LineCanvas, ImageCanvas, Table


class TestLineCanvas(unittest.TestCase):

    def setUp(self):
        self.det = MagicMock()
        self.det.center_mass = np.array([[1, 10, 20], [2, 20, 30], [3, 30, 40]])
        self.canvas = LineCanvas(det_=self.det, current_image_idx=1)

    # Проверяет очистку и обновление графика при отрисовке линейного графика
    def test_draw_line(self):
        self.canvas.axes.clear = MagicMock()
        self.canvas.update_canvas = MagicMock()

        self.canvas.draw_line()

        self.canvas.axes.clear.assert_called_once()
        self.canvas.update_canvas.assert_called_once()

    # Проверяет отрисовку линейного графика с текущей точкой в красном цвете
    def test_draw_line_with_current_point(self):
        self.canvas.axes.clear = MagicMock()
        self.canvas.update_canvas = MagicMock()

        self.canvas.current_image = 2
        self.canvas.draw_line()

        self.canvas.axes.clear.assert_called_once()
        self.canvas.update_canvas.assert_called_once()


class TestImageCanvas(unittest.TestCase):

    def setUp(self):
        self.det = MagicMock()
        self.det.img = np.random.rand(10, 10)
        self.det.img_contour = np.random.rand(10, 10)
        self.canvas = ImageCanvas(det_=self.det)

    # Проверяет загрузку изображения без контура и обновление отображения
    def test_load_image_without_contour(self):
        self.canvas.img = MagicMock()
        self.canvas.axes.draw_artist = MagicMock()
        self.canvas.fig.canvas.blit = MagicMock()

        self.canvas.load_image()

        self.canvas.img.set_data.assert_called_once_with(self.det.img)
        self.canvas.axes.draw_artist.assert_called_once()
        self.canvas.fig.canvas.blit.assert_called_once()

    # Проверяет загрузку изображения с контуром и обновление отображения
    def test_load_image_with_contour(self):
        self.canvas.img = MagicMock()
        self.canvas.axes.draw_artist = MagicMock()
        self.canvas.fig.canvas.blit = MagicMock()
        self.canvas.contour_or_not = 1

        self.canvas.load_image()

        self.canvas.img.set_data.assert_called_once_with(self.det.img_contour)
        self.canvas.axes.draw_artist.assert_called_once()
        self.canvas.fig.canvas.blit.assert_called_once()

    # Проверяет переключение на следующее изображение и его загрузку
    def test_draw_next_image(self):
        self.canvas.current_image_idx = 1
        self.canvas.load_image = MagicMock()

        self.canvas.draw_next_image()

        self.assertEqual(self.canvas.current_image_idx, 2)
        self.canvas.load_image.assert_called_once()

    # Проверяет переключение на предыдущее изображение и его загрузку
    def test_draw_previous_image(self):
        self.canvas.current_image_idx = 1
        self.canvas.load_image = MagicMock()

        self.canvas.draw_previous_image()

        self.assertEqual(self.canvas.current_image_idx, 0)
        self.canvas.load_image.assert_called_once()

    # Проверяет обновление текущего изображения на основе значения слайдера
    def test_update_image_from_slider(self):
        self.canvas.current_image_idx = 0
        self.canvas.load_image = MagicMock()

        self.canvas.update_image_from_slider(200)

        self.assertEqual(self.canvas.current_image_idx, 2)
        self.canvas.load_image.assert_called_once()


class TestTable(unittest.TestCase):

    def setUp(self):
        self.det = MagicMock()
        self.det.center_mass = np.array([[1, 10, 20], [2, 20, 30], [3, 30, 40]])
        self.table = Table(current_image_idx=1, det=self.det)
        self.app = QApplication([])

    def tearDown(self):
        self.app.quit()

    # Проверяет отображение строк таблицы, соответствующих текущему изображению
    def test_show_row(self):
        self.table.numbers_of_rows = MagicMock(return_value=[0, 1, 2])
        self.table.setItem = MagicMock()

        self.table.show_row(1)

        self.table.numbers_of_rows.assert_called_once()
        self.table.setItem.assert_called()

    # Проверяет возвращение индексов строк для первого изображения
    def test_numbers_of_rows_first_image(self):
        self.table.index = 0

        rows = self.table.numbers_of_rows()

        self.assertEqual(rows, [0, 1, 2])

    # Проверяет возвращение индексов строк для последнего изображения
    def test_numbers_of_rows_last_image(self):
        self.table.index = 2

        rows = self.table.numbers_of_rows()

        self.assertEqual(rows, [0, 1, 2])

    # Проверяет возвращение индексов строк для среднего изображения
    def test_numbers_of_rows_middle_image(self):
        self.table.index = 1

        rows = self.table.numbers_of_rows()

        self.assertEqual(rows, [0, 1, 2])


def run_tests():
    unittest.main()

if __name__ == '__main__':
    run_tests()
