import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import (
    QApplication,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QLabel,
    QTableWidgetItem,
    QTableWidget, QSlider,
)
from widgets import LineCanvas, ImageCanvas, Table

import os
counter = 0

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Center of mass of the drop")

        # Create a QVBoxLayout instance
        layout = QVBoxLayout()
        line_layout = QHBoxLayout()
        buttons_layot =  QHBoxLayout()

        # Add widgets to the layout
        button1 = QPushButton("Предыдущее изображение")
        button2 = QPushButton("Следующее изображение")
        lineCanvas = LineCanvas(self)
        imgCanvas = ImageCanvas(self)


        def button3_clicked():
            global counter
            counter += 1
            if counter % 2 == 1:
                imgCanvas.folder_path= "exp2"
            else:
                imgCanvas.folder_path= "exp1"

        def button1_clicked():
            imgCanvas.draw_previous_image()
            table.show_row(imgCanvas.current_image_idx)

        def button2_clicked():
            imgCanvas.draw_next_image()
            table.show_row(imgCanvas.current_image_idx)

        table = Table('koord.csv', imgCanvas.current_image_idx)
        table.show()
        button3 = QPushButton("Включить режим контура капли")
        button3.clicked.connect(button3_clicked)
        button1.clicked.connect(button1_clicked)
        button2.clicked.connect(button2_clicked)


        line_layout.addWidget(lineCanvas)

        img_layout = QtWidgets.QVBoxLayout()
        img_layout.addWidget(imgCanvas)
        img_layout.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)  # Center the image vertically and horizontally
        img_table_layout = QtWidgets.QHBoxLayout()
        img_table_layout.addStretch()
        table.setFixedWidth(475)
        img_table_layout.addWidget(table)
        img_table_layout.addStretch()
        img_layout.addLayout(img_table_layout)

        line_layout.addLayout(img_layout)
        layout.addLayout(line_layout)

        # Add the two QHBoxLayouts to the main QHBoxLayout
        line_layout.addLayout(img_table_layout)
        layout.addLayout(line_layout)


        buttons_layot.addWidget(button1)
        buttons_layot.addWidget(button2)
        layout.addLayout(buttons_layot)
        layout.addWidget(button3)

        # Set the layout on the application's window
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
