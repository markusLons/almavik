import sys
import pytest
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

@fixture(scope='session')
def qt_app(request):
    app = QApplication([])
    yield app
    app.quit()

@fixture
def qtbot(app):
    return QtBot(app)

@fixture
def window(qtbot):
    det = detectorDrop(exp1_dir)
    window = Window(det)
    window.show()
    qtbot.addWidget(window)
    yield window
    window.close()


def test_window_title(window):
    assert window.windowTitle() == "Center of mass of the drop"


