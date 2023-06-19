import sys
from PyQt5.QtWidgets import QWidget
import unittest
from PyQt5.QtWidgets import QApplication

sys.path.insert(1, 'src/')
from widgets import MplCanvas, LineCanvas, ImageCanvas, Table

from matplotlib.figure import Figure
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg

class TestMplCanvas(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])
        self.canvas = MplCanvas()

    def test_canvas_initialization(self):
        self.assertIsInstance(self.canvas.fig, Figure)
        self.assertIsInstance(self.canvas, FigureCanvasQTAgg)
        self.assertIsNotNone(self.canvas.axes)

    def test_update_canvas(self):
        # Создаем фиктивный график
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        self.canvas.axes.plot(x, y)

        # Обновляем холст
        self.canvas.update_canvas()

        # Проверяем, что график был успешно обновлен
        self.assertEqual(len(self.canvas.fig.axes), 1)
        self.assertEqual(len(self.canvas.fig.axes[0].lines), 1)


class TestLineCanvas(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])
        self.det_ = 10  
        self.canvas = LineCanvas(self.det_)

    def test_draw_line(self):
        # Устанавливаем тестовые данные для графика
        self.canvas.data = [[0, 0, 0], [1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5]]
        self.canvas.current_image = 3

        # Рисуем линию
        self.canvas.draw_line()

        # Проверяем, что линия была успешно нарисована
        self.assertEqual(len(self.canvas.axes.lines), 2)  # 1 линия для данных и 1 линия для текущей точки


class TestImageCanvas(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])
        self.det_ = 10
        self.canvas = ImageCanvas(self.det_)

    def test_load_image(self):
        # Устанавливаем тестовое изображение
        image = np.random.rand(100, 100)
        self.canvas.img_without_contour = [image]

        # Загружаем изображение
        self.canvas.load_image()

        # Проверяем, что изображение было успешно загружено
        self.assertEqual(len(self.canvas.axes.images), 1)

    def test_draw_next_image(self):
        # Устанавливаем тестовые данные
        self.canvas.current_image_idx = 0
        self.canvas.img_without_contour = [np.random.rand(100, 100)] * 3

        # Рисуем следующее изображение
        self.canvas.draw_next_image()

        # Проверяем, что следующее изображение было успешно загружено
        self.assertEqual(self.canvas.current_image_idx, 1)

    def test_draw_previous_image(self):
        # Устанавливаем тестовые данные
        self.canvas.current_image_idx = 2
        self.canvas.img_without_contour = [np.random.rand(100, 100)] * 3

        # Рисуем предыдущее изображение
        self.canvas.draw_previous_image()

        # Проверяем, что предыдущее изображение было успешно загружено
        self.assertEqual(self.canvas.current_image_idx, 1)

    def test_update_image_from_slider(self):
        # Устанавливаем тестовые данные
        self.canvas.current_image_idx = 0
        self.canvas.img_without_contour = [np.random.rand(100, 100)] * 10

        # Обновляем изображение на основе значения слайдера
        value = 5
        self.canvas.update_image_from_slider(value)

        # Проверяем, что изображение было успешно обновлено
        self.assertEqual(self.canvas.current_image_idx, 5)


class TestTable(unittest.TestCase):
    def setUp(self):
        self.current_image_idx = 0  # Замените на свои тестовые данные
        self.det = 10
        self.table = Table(self.current_image_idx, self.det)

    def test_show_row(self):
        # Устанавливаем тестовые данные
        self.table.data = [[0, 0, 0], [1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]
        self.table.index = 2

        # Показываем строки таблицы, соответствующие текущему индексу изображения
        self.table.show_row(self.table.index)

        # Получаем значения из отображенных строк таблицы
        row_values = []
        for row_idx in range(self.table.table.rowCount()):
            row_values.append([self.table.table.item(row_idx, col_idx).text()
                               for col_idx in range(self.table.table.columnCount())])

        # Проверяем, что значения в строках таблицы соответствуют ожидаемым значениям
        expected_values = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
        self.assertEqual(row_values, expected_values)

    def test_numbers_of_rows(self):
        # Устанавливаем тестовые данные
        self.table.data = [[0, 0, 0], [1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]
        self.table.index = 0

        # Получаем индексы строк, которые должны быть отображены в таблице
        row_indices = self.table.numbers_of_rows()

        # Проверяем, что полученные индексы соответствуют ожидаемым значениям
        expected_indices = [0, 1, 2]
        self.assertEqual(row_indices, expected_indices)


if __name__ == '__main__':
    unittest.main()
