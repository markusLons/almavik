import sys
from PyQt5.QtWidgets import QApplication
from pytestqt.plugin import QtBot
from PyQt5.QtCore import Qt
from PyQt5.QtTest import QTest
from pytest import fixture
import os

sys.path.insert(1, 'src/')
from YPPRPO import Window, detectorDrop

current_dir = os.path.dirname(os.path.abspath(__file__))
exp1_dir = os.path.join(current_dir, '../exp1')

@fixture
def window(qtbot):
    app = QApplication(sys.argv)
    det = detectorDrop(exp1_dir)
    window = Window(det)
    window.show()
    qtbot.addWidget(window)
    yield window
    window.close()


def test_window_title(window):
    assert window.windowTitle() == "Center of mass of the drop"


def test_slider_value(window, qtbot):
    slider = window.slider
    qtbot.waitSignal(slider.valueChanged, timeout=2000)
    assert slider.value() == 0
    QTest.mouseClick(slider, Qt.LeftButton, pos=slider.rect().topRight())
    qtbot.waitSignal(slider.valueChanged, timeout=2000)
    assert slider.value() == 400


def test_button1_clicked(window, qtbot):
    button1 = window.button1
    slider = window.slider
    initial_value = slider.value()
    qtbot.mouseClick(button1, Qt.LeftButton)
    qtbot.wait(2000)  # Wait for the image to load or update
    assert slider.value() == initial_value - 1


def test_button2_clicked(window, qtbot):
    button2 = window.button2
    slider = window.slider
    initial_value = slider.value()
    qtbot.mouseClick(button2, Qt.LeftButton)
    qtbot.wait(2000)  # Wait for the image to load or update
    assert slider.value() == initial_value + 1


def test_button3_clicked(window, qtbot):
    button3 = window.button3
    initial_text = button3.text()
    qtbot.mouseClick(button3, Qt.LeftButton)
    qtbot.wait(2000)  # Wait for the image to load or update
    assert button3.text() != initial_text


def test_table_show_row(window, qtbot):
    slider = window.slider
    table = window.table
    initial_row = table.currentRow()
    qtbot.waitSignal(table.currentCellChanged, timeout=2000)
    assert table.currentRow() == initial_row
    QTest.mouseClick(slider, Qt.LeftButton, pos=slider.rect().topRight())
    qtbot.waitSignal(table.currentCellChanged, timeout=2000)
    assert table.currentRow() != initial_row


def test_initial_image(window):
    imgCanvas = window.imgCanvas
    assert imgCanvas.current_image_idx == 0


def test_next_image(window, qtbot):
    imgCanvas = window.imgCanvas
    initial_image = imgCanvas.current_image_idx
    button2 = window.button2
    qtbot.mouseClick(button2, Qt.LeftButton)
    qtbot.wait(2000)  # Wait for the image to load or update
    assert imgCanvas.current_image_idx == initial_image + 1


def test_previous_image(window, qtbot):
    imgCanvas = window.imgCanvas
    initial_image = imgCanvas.current_image_idx
    button1 = window.button1
    qtbot.mouseClick(button1, Qt.LeftButton)
    qtbot.wait(2000)  # Wait for the image to load or update
    assert imgCanvas.current_image_idx == initial_image - 1

if __name__ == '__main__':
    pytest.main()
