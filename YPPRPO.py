import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QLabel,
    QTableWidgetItem,
    QTableWidget,
    QSlider,
)
from widgets import LineCanvas, ImageCanvas, Table
from detectorDrop import detectorDrop

counter = 0

class Window(QWidget):
    def __init__(self, det):
        self.det = det
        super().__init__()
        self.setWindowTitle("Center of mass of the drop")

        layout = QVBoxLayout()
        line_layout = QHBoxLayout()
        buttons_layot = QHBoxLayout()

        self.slider_label = QLabel("0")
        self.slider_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.slider_label)

        button1 = QPushButton("Предыдущее изображение")
        button2 = QPushButton("Следующее изображение")
        imgCanvas = ImageCanvas(det_ = det)
        lineCanvas = LineCanvas(det_=det, current_image_idx=imgCanvas.current_image_idx)

        def slider_value_changed():
            table.show_row(imgCanvas.current_image_idx)
            lineCanvas.current_image = slider.value()
            lineCanvas.draw_line()

        slider = QSlider()
        slider.setOrientation(Qt.Horizontal)
        slider.setRange(0, 401)
        slider.setValue(0)
        slider.setTickInterval(1)
        slider.setTickPosition(QSlider.TicksBelow)
        slider.valueChanged.connect(imgCanvas.update_image_from_slider)
        slider.valueChanged.connect(slider_value_changed)


        def button3_clicked():
            global counter
            counter += 1
            if counter % 2 == 1:
                imgCanvas.contour_or_not=1
                button3.setText("Выключить режим контура капли")
            else:
                imgCanvas.contour_or_not=0
                button3.setText("Включить режим контура капли")

        def button1_clicked():
            imgCanvas.draw_previous_image()
            lineCanvas.current_image=imgCanvas.current_image_idx
            table.show_row(imgCanvas.current_image_idx)
            slider.setValue(imgCanvas.current_image_idx)
            lineCanvas.draw_line()

        def button2_clicked():
            imgCanvas.draw_next_image()
            lineCanvas.current_image = imgCanvas.current_image_idx
            table.show_row(imgCanvas.current_image_idx)
            slider.setValue(imgCanvas.current_image_idx)
            lineCanvas.draw_line()

        lineCanvas.draw_line()
        table = Table(imgCanvas.current_image_idx, det)
        table.show()

        button3 = QPushButton("Включить режим контура капли")
        button3.clicked.connect(button3_clicked)
        button1.clicked.connect(button1_clicked)
        button2.clicked.connect(button2_clicked)

        label = QLabel(str(slider.value()))
        slider.valueChanged.connect(lambda value: label.setText(str(value)))

        line_slider_layot=QtWidgets.QVBoxLayout()
        line_slider_layot.addWidget(lineCanvas)
        line_slider_layot.addWidget(slider)
        img_layout = QtWidgets.QVBoxLayout()
        img_layout.addWidget(imgCanvas)
        img_layout.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        img_table_layout = QtWidgets.QHBoxLayout()
        img_table_layout.addStretch()
        table.setFixedWidth(475)
        img_table_layout.addWidget(table)
        img_table_layout.addStretch()
        img_layout.addLayout(img_table_layout)

        line_layout.addLayout(line_slider_layot)
        line_layout.addLayout(img_layout)
        layout.addLayout(line_layout)

        line_layout.addLayout(img_table_layout)
        layout.addLayout(line_layout)


        buttons_layot.addWidget(button1)
        buttons_layot.addWidget(button2)
        layout.addLayout(buttons_layot)
        layout.addWidget(button3)

        self.setLayout(layout)


if __name__ == "__main__":
    folder_path = "exp1"
    det =detectorDrop(folder_path)
    app = QApplication(sys.argv)
    window = Window(det)
    window.show()
    sys.exit(app.exec_())
