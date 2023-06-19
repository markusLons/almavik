import sys
from PyQt5.QtWidgets import QWidget
import unittest
from PyQt5.QtWidgets import QApplication

sys.path.insert(1, 'src/')
from widgets import MplCanvas, LineCanvas, ImageCanvas, Table
from unittest.mock import MagicMock

class TestLineCanvas(unittest.TestCase):
    def test_draw_line(self):
        # Создаем экземпляр LineCanvas
        canvas = LineCanvas()

        # Задаем тестовые данные
        canvas.data = [[1, 10, 20], [2, 15, 25], [3, 12, 18], [4, 8, 22], [5, 11, 17]]
        canvas.current_image = 2

        # Вызываем метод draw_line()
        canvas.draw_line()

        # Проверяем, что линия была нарисована
        self.assertEqual(len(canvas.axes.lines), 2)

        # Проверяем, что текущая точка была нарисована
        self.assertEqual(len(canvas.axes.lines[1].get_xydata()), 1)

        # Проверяем, что границы осей были установлены
        self.assertIsNotNone(canvas.axes.get_xlim())
        self.assertIsNotNone(canvas.axes.get_ylim())


class TestImageCanvas(unittest.TestCase):
    def test_load_image(self):
        # Создаем экземпляр ImageCanvas
        canvas = ImageCanvas()

        # Задаем тестовые данные
        canvas.img_without_contour = [MagicMock(), MagicMock(), MagicMock()]
        canvas.img_with_contour = [MagicMock(), MagicMock(), MagicMock()]
        canvas.current_image_idx = 1
        canvas.contour_or_not = 0

        # Вызываем метод load_image()
        canvas.load_image()

        # Проверяем, что изображение было успешно загружено
        self.assertIsNotNone(canvas.img)


class TestTable(unittest.TestCase):
    def test_show_row(self):
        # Создаем экземпляр Table
        table = Table(current_image_idx=2, det=MagicMock())

        # Вызываем метод show_row()
        table.show_row(current_image_idx=3)

        # Проверяем, что строки таблицы были успешно обновлены
        self.assertIsNotNone(table.table.item(0, 0))
        self.assertIsNotNone(table.table.item(0, 1))
        self.assertIsNotNone(table.table.item(0, 2))

if __name__ == '__main__':
    unittest.main()
