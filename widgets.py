import os
import csv

import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QHBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure
from PyQt5 import QtWidgets


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=7, height=7, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        super(MplCanvas, self).__init__(self.fig)
        self.axes = self.fig.add_subplot(1, 1, 1)
        self.fig.tight_layout()

    def update_canvas(self):
        self.fig.canvas.draw()


class LineCanvas(MplCanvas):
    def __init__(self, parent=None, width=7, height=7, dpi=100):
        super().__init__()
        self.line = None

    def draw_random_line(self):
        if self.line is None:
            self.line, = self.axes.plot(np.arange(100), np.random.rand(100), linewidth=.8, color="red", marker='s')
        self.line.set_ydata(np.random.rand(100))
        self.update_canvas()


class ImageCanvas(MplCanvas):
    def __init__(self, parent=None, width=7, height=7, dpi=100):
        super().__init__()
        self.img = None
        self.axes.axis("off")
        self.current_image_idx = 0
        self.folder_path = "exp1"
        self.image_paths = self.get_image_paths()
        self.load_image(self.image_paths[self.current_image_idx])

    def get_image_paths(self):
        image_extensions = [".jpg", ".jpeg", ".png"]
        image_paths = []
        for file_name in os.listdir(self.folder_path):
            if os.path.splitext(file_name)[1].lower() in image_extensions:
                image_paths.append(os.path.join(self.folder_path, file_name))
        return image_paths

    def load_image(self, image_path):
        image = plt.imread(image_path)
        self.img = self.axes.imshow(image, cmap="gray")
        self.update_canvas()

    def draw_next_image(self):
        image_paths = self.get_image_paths()
        if (self.current_image_idx % (len(image_paths) - 1) != 0 or self.current_image_idx != len(image_paths) - 1):
            self.current_image_idx = (self.current_image_idx + 1) % len(image_paths)
        image_path = image_paths[self.current_image_idx]
        self.load_image(image_path)

    def draw_previous_image(self):
        image_paths = self.get_image_paths()
        if ((self.current_image_idx) % len(image_paths) != 0):
            self.current_image_idx = (self.current_image_idx - 1) % len(image_paths)
        image_path = image_paths[self.current_image_idx]
        self.load_image(image_path)

    def update_image_from_slider(self, value):
        max_slider_value = 401
        image_index = int(value * len(self.image_paths) / max_slider_value)
        self.current_image_idx = image_index
        image_path = self.image_paths[self.current_image_idx]
        self.load_image(image_path)


class Table(QWidget):
    def __init__(self, filename, current_image_idx):
        super().__init__()
        self.data = []
        with open(filename) as f:
            reader = csv.reader(f)
            for row in reader:
                self.data.append(row)

        self.table = QTableWidget()
        self.table.setColumnCount(len(self.data[0]))
        self.table.setRowCount(3)
        self.table.setVerticalHeaderLabels(["Previous", "Now", "Next"])
        self.table.setHorizontalHeaderLabels(["Number", "x", "y"])

        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                item = QTableWidgetItem(self.data[i][j])
                self.table.setItem(i, j, item)

        layout = QHBoxLayout()
        layout.addWidget(self.table)

        self.setLayout(layout)
        self.index = 0
        self.show_row(current_image_idx)

    def show_row(self, current_image_idx):
        self.index = current_image_idx
        row_indices = self.numbers_of_rows()
        for row_idx, data_idx in enumerate(row_indices):
            for col_idx in range(len(self.data[data_idx])):
                item = QTableWidgetItem(self.data[data_idx][col_idx])
                self.table.setItem(row_idx, col_idx, item)

    def numbers_of_rows(self):
        row_indices = []
        if self.index == 0:
            row_indices.extend([0, 1, 2])
        else:
            if self.index == len(self.data) - 1:
                row_indices.extend([self.index - 2, self.index - 1, self.index])
            else:
                row_indices.extend([self.index - 1, self.index, self.index + 1])
        return row_indices
