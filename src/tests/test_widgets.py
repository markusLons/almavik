import pytest
from PyQt5.QtWidgets import QApplication
import sys

sys.path.insert(1, 'src/')
from widgets import MplCanvas, LineCanvas, ImageCanvas, Table

@pytest.fixture
def app():
    # Инициализация QApplication
    app = QApplication([])
    yield app
    app.quit()


def test_mpl_canvas(app):
    # Создание экземпляра MplCanvas
    canvas = MplCanvas()
    
    # Проверка, что canvas является экземпляром QWidget
    assert isinstance(canvas, QWidget)
    
    # Проверка значений по умолчанию
    assert canvas.fig.get_figwidth() == 7
    assert canvas.fig.get_figheight() == 7
    assert canvas.fig.get_dpi() == 100
    
    # Проверка метода update_canvas
    canvas.update_canvas()


def test_line_canvas(app):
    # Создание экземпляра LineCanvas
    canvas = LineCanvas()
    
    # Проверка, что canvas является экземпляром MplCanvas
    assert isinstance(canvas, MplCanvas)
    
    # Проверка значений по умолчанию
    assert canvas.line is None
    assert isinstance(canvas.data, list)
    
    # Проверка метода draw_line
    canvas.draw_line()


def test_image_canvas(app):
    # Создание экземпляра ImageCanvas
    canvas = ImageCanvas()
    
    # Проверка, что canvas является экземпляром MplCanvas
    assert isinstance(canvas, MplCanvas)
    
    # Проверка значений по умолчанию
    assert canvas.img is None
    assert isinstance(canvas.img_without_contour, list)
    assert isinstance(canvas.img_with_contour, list)
    
    # Проверка методов load_image, draw_next_image, draw_previous_image, update_image_from_slider
    canvas.load_image()
    canvas.draw_next_image()
    canvas.draw_previous_image()
    canvas.update_image_from_slider(50)


def test_table():
    # Создание экземпляра Table
    table = Table(current_image_idx=0, det=None)
    
    # Проверка, что table является экземпляром QWidget
    assert isinstance(table, QWidget)
    
    # Проверка значений по умолчанию
    assert isinstance(table.data, list)
    
    # Проверка методов show_row, numbers_of_rows
    table.show_row(current_image_idx=0)
    row_indices = table.numbers_of_rows()
    assert isinstance(row_indices, list)

