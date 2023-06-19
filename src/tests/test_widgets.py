import pytest
from PyQt5.QtWidgets import QApplication
from almavik.widgets import MplCanvas, LineCanvas, ImageCanvas, Table

@pytest.fixture(scope='module')
def qt_app(request):
    app = QApplication([])
    
    def teardown():
        app.quit()
    
    request.addfinalizer(teardown)
    return app

def test_MplCanvas_update_canvas(qt_app):
    canvas = MplCanvas()
    canvas.update_canvas()
    # No exception should be raised

def test_LineCanvas_draw_line(qt_app):
    canvas = LineCanvas()
    canvas.draw_line()
    # No exception should be raised

def test_ImageCanvas_load_image(qt_app):
    canvas = ImageCanvas()
    canvas.load_image()
    # No exception should be raised

def test_Table_show_row():
    table = Table(current_image_idx=0, det=None)
    table.show_row(current_image_idx=0)
    # No exception should be raised

def test_Table_numbers_of_rows():
    table = Table(current_image_idx=0, det=None)
    row_indices = table.numbers_of_rows()
    assert row_indices == [0, 1, 2]

    table.index = len(table.data) - 1
    row_indices = table.numbers_of_rows()
    assert row_indices == [table.index - 2, table.index - 1, table.index]

    table.index = 1
    row_indices = table.numbers_of_rows()
    assert row_indices == [table.index - 1, table.index, table.index + 1]
