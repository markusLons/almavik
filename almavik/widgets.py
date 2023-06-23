import os
import csv

import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QHBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):
    """
    A canvas for displaying a Matplotlib figure.
    
    Args:
        parent (QWidget): The parent widget.
        width (int): The width of the canvas in inches.
        height (int): The height of the canvas in inches.
        dpi (int): The dots per inch of the canvas.
    """

    def __init__(self, parent=None, width=7, height=7, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        super(MplCanvas, self).__init__(self.fig)
        self.axes = self.fig.add_subplot(1, 1, 1)
        self.fig.tight_layout()

    def update_canvas(self):
        """
        Update the canvas by redrawing the figure.
        """
        self.fig.canvas.draw()


class LineCanvas(MplCanvas):
    """
    A canvas for displaying a line plot of center of mass data.
    
    Args:
        det_ (detectorDrop): The detectorDrop object containing the center of mass data.
        current_image_idx (int): The index of the current image being displayed.
        parent (QWidget): The parent widget.
        width (int): The width of the canvas in inches.
        height (int): The height of the canvas in inches.
        dpi (int): The dots per inch of the canvas.
    """

    def __init__(self, det_=None, current_image_idx=0, parent=None, width=7, height=7, dpi=100):
        super().__init__()
        self.line = None
        self.data = [list(row) for row in det_.center_mass]
        self.current_image = current_image_idx

    def draw_line(self):
        """
        Draw the line plot of the center of mass data.
        """
        self.axes.clear()

        start_idx = 0
        end_idx = len(self.data)

        data_to_plot = self.data[start_idx:end_idx]
        x_data = [row[1] for row in data_to_plot]
        y_data = [row[2] for row in data_to_plot]

        self.axes.plot(x_data, y_data, color='black', linestyle='solid', marker='o')

        current_point = data_to_plot[self.current_image - start_idx]
        self.axes.plot(current_point[1], current_point[2], color='red', linestyle='solid', marker='o')

        self.axes.set_xlim(min(x_data) - 10, max(x_data) + 10)
        self.axes.set_ylim(min(y_data) - 10, max(y_data) + 10)

        self.update_canvas()


class ImageCanvas(MplCanvas):
    """
    A canvas for displaying images with optional contour overlay.
    
    Args:
        det_ (detectorDrop): The detectorDrop object containing the image data.
        parent (QWidget): The parent widget.
        width (int): The width of the canvas in inches.
        height (int): The height of the canvas in inches.
        dpi (int): The dots per inch of the canvas.
    """

    def __init__(self, det_=None, parent=None, width=7, height=7, dpi=100):
        super().__init__()
        self.img = None
        self.axes.axis("off")
        self.current_image_idx = 0
        self.contour_or_not = 0
        self.img_without_contour = det_.img
        self.img_with_contour = det_.img_contour

        self.image_paths = [f"Image {i}" for i in range(len(self.img_without_contour))]
        self.load_image()

    def load_image(self):
        """
        Load and display the current image.
        """
        if self.contour_or_not == 0:
            image = self.img_without_contour[self.current_image_idx]
        else:
            image = self.img_with_contour[self.current_image_idx]

        if self.img is None:
            self.img = self.axes.imshow(image, cmap="gray")
        else:
            self.img.set_data(image)
            self.axes.draw_artist(self.img)
            self.fig.canvas.blit(self.axes.bbox)

    def draw_next_image(self):
        """
        Increment the current image index and load the next image.
        """
        if self.current_image_idx < len(self.image_paths) - 1:
            self.current_image_idx += 1
            self.load_image()

    def draw_previous_image(self):
        """
        Decrement the current image index and load the previous image.
        """
        if self.current_image_idx > 0:
            self.current_image_idx -= 1
            self.load_image()

    def update_image_from_slider(self, value):
        """
        Update the current image based on the value of a slider.
        
        Args:
            value (int): The value of the slider.
        """
        value = value % 400
        max_slider_value = len(self.img_without_contour) - 1
        image_index = int(value * len(self.image_paths) / max_slider_value)
        self.current_image_idx = image_index
        self.load_image()


class Table(QWidget):
    """
    A table widget for displaying center of mass data.
    
    Args:
        current_image_idx (int): The index of the current image being displayed.
        det (detectorDrop): The detectorDrop object containing the center of mass data.
    """

    def __init__(self, current_image_idx, det):
        super().__init__()

        self.data = [list(row) for row in det.center_mass]
        self.table = QTableWidget()
        self.table.setColumnCount(len(self.data[0]))
        self.table.setRowCount(3)
        self.table.setVerticalHeaderLabels(["Previous", "Now", "Next"])
        self.table.setHorizontalHeaderLabels(["Number", "x", "y"])

        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                item = QTableWidgetItem(str(self.data[i][j]))
                self.table.setItem(i, j, item)

        layout = QHBoxLayout()
        layout.addWidget(self.table)

        self.setLayout(layout)
        self.index = 0
        self.show_row(current_image_idx)

    def show_row(self, current_image_idx):
        """
        Show the rows of the table corresponding to the current image index.
        
        Args:
            current_image_idx (int): The index of the current image being displayed.
        """
        self.index = current_image_idx
        row_indices = self.numbers_of_rows()
        for row_idx, data_idx in enumerate(row_indices):
            for col_idx in range(len(self.data[data_idx])):
                item = QTableWidgetItem(str(self.data[data_idx][col_idx]))
                self.table.setItem(row_idx, col_idx, item)

    def numbers_of_rows(self):
        """
        Return the row indices to be shown in the table based on the current image index.
        
        Returns:
            list: A list of row indices.
        """
        row_indices = []
        if self.index == 0:
            row_indices.extend([0, 1, 2])
        else:
            if self.index == len(self.data) - 1:
                row_indices.extend([self.index - 2, self.index - 1, self.index])
            else:
                row_indices.extend([self.index - 1, self.index, self.index + 1])
        return row_indices
