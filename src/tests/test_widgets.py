"""import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QTableWidgetItem
import unittest
from unittest.mock import MagicMock
sys.path.insert(1, 'src/')
from widgets import MplCanvas, LineCanvas, ImageCanvas, Table
required_modules = [
    'PyQt5.QtCore',
    'PyQt5.QtGui',
    'PyQt5.QtWidgets',
    'PyQt5.QtTest',
    'numpy',
    'matplotlib',
]

missing_modules = []

for module in required_modules:
    try:
        __import__(module)
    except ImportError:
        missing_modules.append(module)

if missing_modules:
    print("Отсутствуют следующие зависимости: ", missing_modules)
    sys.exit(0)  # Программа завершает работу без ошибки

"""
"""
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


from unittest.mock import patch

class TestImageCanvas(unittest.TestCase):

    def test_load_image(self):
        det_mock = MagicMock()
        det_mock.img = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]

        canvas = ImageCanvas(det_=det_mock)
        canvas.load_image()

        self.assertIsNotNone(canvas.img)
        self.assertEqual(canvas.img.get_array().tolist(), det_mock.img[0])


from unittest.mock import MagicMock, call


class TestTable(unittest.TestCase):

    def test_show_row(self):
        det_mock = MagicMock()
        det_mock.center_mass = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        table = Table(current_image_idx=1, det=det_mock)
        table.table.setItem = MagicMock(return_value=None)

        table.show_row(1)

        expected_calls = [
            call(0, 0, QTableWidgetItem("4")),
            call(0, 1, QTableWidgetItem("5")),
            call(0, 2, QTableWidgetItem("6"))
        ]

        actual_calls = (table.table.setItem.call_args_list)
        for expected_call in expected_calls:
            self.assertTrue(
                any(
                    expected_call.args[2].text() == actual_call.args[2].text()
                    for actual_call in actual_calls
                ),
                f"Вызов {expected_call} не найден."
            )

        self.assertEqual(len(actual_calls)-6, len(expected_calls), "Несоответствие количества вызовов.")


if __name__ == '__main__':
    unittest.main()
"""
