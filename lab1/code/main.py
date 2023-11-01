import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QLabel, QPushButton, QColorDialog, QGridLayout, QWidget, QLineEdit, QSlider
from PyQt5.QtCore import Qt
from color_converter import ColorConverter
from PyQt5.QtGui import QColor

slider_style = """
        QSlider::groove:horizontal {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #bbb, stop:1 #ccc);
            border: 1px solid #777;
            height: 10px;
            border-radius: 4px;
        }
        
        QSlider::handle:horizontal {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #eee, stop:1 #ccc);
            border: 1px solid #777;
            width: 18px;
            margin: -2px 0;
            border-radius: 4px;
        }
    """


class SimpleApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.c = 0
        self.m = 0
        self.ys = 0
        self.k = 0
        self.r = 0
        self.g = 0
        self.b = 0
        self.h = 0
        self.s = 0
        self.v = 0
        
        # Создаем основное окно
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Создаем макет для размещения виджетов
        self.layout = QGridLayout()

        self.create_labels()
        self.set_labels_position()
        self.create_line_editors()
        self.set_line_editors_position()
        self.create_sliders()
        self.set_sliders_position()
        self.create_color_rectangle()
        self.create_palette()


        # Назначаем макет как центральный виджет
        central_widget.setLayout(self.layout)
    
    def show_color_dialog(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.r = int(color.red())
            self.g = int(color.green())
            self.b = int(color.blue())
        self.update_from_rgb_ledit()

    def create_palette(self):
        self.color_button = QPushButton('Choose color')
        self.color_button.clicked.connect(self.show_color_dialog)
        self.layout.addWidget(self.color_button, 9, 6, 1, 5)


    def create_labels(self):
        self.c_label = QLabel('C:')
        self.m_label = QLabel('M:')
        self.y_label = QLabel('Y:')
        self.k_label = QLabel('K:')

        self.r_label = QLabel('R:')
        self.g_label = QLabel('G:')
        self.b_label = QLabel('B:')

        self.h_label = QLabel('H:')
        self.s_label = QLabel('S:')
        self.v_label = QLabel('V:')
    
    def set_labels_position(self):
        self.layout.addWidget(self.c_label, 0, 0)
        self.layout.addWidget(self.m_label, 1, 0)
        self.layout.addWidget(self.y_label, 2, 0)
        self.layout.addWidget(self.k_label, 3, 0)

        self.layout.addWidget(self.r_label, 4, 0)
        self.layout.addWidget(self.g_label, 5, 0)
        self.layout.addWidget(self.b_label, 6, 0)

        self.layout.addWidget(self.h_label, 7, 0)
        self.layout.addWidget(self.s_label, 8, 0)
        self.layout.addWidget(self.v_label, 9, 0)

    def create_line_editors(self):
        self.c_ledit = QLineEdit()
        self.c_ledit.setFixedWidth(30)
        self.c_ledit.editingFinished.connect(self.on_c_ledit_change)
        self.m_ledit = QLineEdit()
        self.m_ledit.setFixedWidth(30)
        self.m_ledit.editingFinished.connect(self.on_m_ledit_change)
        self.y_ledit = QLineEdit()
        self.y_ledit.setFixedWidth(30)
        self.y_ledit.editingFinished.connect(self.on_y_ledit_change)
        self.k_ledit = QLineEdit()
        self.k_ledit.setFixedWidth(30)
        self.k_ledit.editingFinished.connect(self.on_k_ledit_change)

        self.r_ledit = QLineEdit()
        self.r_ledit.setFixedWidth(30)
        self.r_ledit.editingFinished.connect(self.on_r_ledit_change)
        self.g_ledit = QLineEdit()
        self.g_ledit.setFixedWidth(30)
        self.g_ledit.editingFinished.connect(self.on_g_ledit_change)
        self.b_ledit = QLineEdit()
        self.b_ledit.setFixedWidth(30)
        self.b_ledit.editingFinished.connect(self.on_b_ledit_change)

        self.h_ledit = QLineEdit()
        self.h_ledit.setFixedWidth(30)
        self.h_ledit.editingFinished.connect(self.on_h_ledit_change)
        self.s_ledit = QLineEdit()
        self.s_ledit.setFixedWidth(30)
        self.s_ledit.editingFinished.connect(self.on_s_ledit_change)
        self.v_ledit = QLineEdit()
        self.v_ledit.setFixedWidth(30)
        self.v_ledit.editingFinished.connect(self.on_v_ledit_change)
    

    
    def set_line_editors_position(self):
        self.layout.addWidget(self.c_ledit, 0, 1)
        self.layout.addWidget(self.m_ledit, 1, 1)
        self.layout.addWidget(self.y_ledit, 2, 1)
        self.layout.addWidget(self.k_ledit, 3, 1)

        self.layout.addWidget(self.r_ledit, 4, 1)
        self.layout.addWidget(self.g_ledit, 5, 1)
        self.layout.addWidget(self.b_ledit, 6, 1)

        self.layout.addWidget(self.h_ledit, 7, 1)
        self.layout.addWidget(self.s_ledit, 8, 1)
        self.layout.addWidget(self.v_ledit, 9, 1)

    def create_slider(self, minimum, maximum):
        slider = QSlider(Qt.Horizontal)
        slider.setMaximum(maximum)
        slider.setMinimum(minimum)
        slider.setStyleSheet(slider_style)
        return slider

    def create_sliders(self):
        self.c_slider = self.create_slider(0, 100)
        self.c_slider.valueChanged.connect(self.on_c_slider_change)
        self.m_slider = self.create_slider(0, 100)
        self.m_slider.valueChanged.connect(self.on_m_slider_change)
        self.y_slider = self.create_slider(0, 100)
        self.y_slider.valueChanged.connect(self.on_y_slider_change)
        self.k_slider = self.create_slider(0, 100)
        self.k_slider.valueChanged.connect(self.on_k_slider_change)

        self.r_slider = self.create_slider(0, 255)
        self.r_slider.valueChanged.connect(self.on_r_slider_change)
        self.g_slider = self.create_slider(0, 255)
        self.g_slider.valueChanged.connect(self.on_g_slider_change)
        self.b_slider = self.create_slider(0, 255)
        self.b_slider.valueChanged.connect(self.on_b_slider_change)

        self.h_slider = self.create_slider(0, 360)
        self.h_slider.valueChanged.connect(self.on_h_slider_change)
        self.s_slider = self.create_slider(0, 100)
        self.s_slider.valueChanged.connect(self.on_s_slider_change)
        self.v_slider = self.create_slider(0, 100)
        self.v_slider.valueChanged.connect(self.on_v_slider_change)

    def set_sliders_position(self):
        self.layout.addWidget(self.c_slider, 0, 2, 1, 4)
        self.layout.addWidget(self.m_slider, 1, 2, 1, 4)
        self.layout.addWidget(self.y_slider, 2, 2, 1, 4)
        self.layout.addWidget(self.k_slider, 3, 2, 1, 4)

        self.layout.addWidget(self.r_slider, 4, 2, 1, 4)
        self.layout.addWidget(self.g_slider, 5, 2, 1, 4)
        self.layout.addWidget(self.b_slider, 6, 2, 1, 4)

        self.layout.addWidget(self.h_slider, 7, 2, 1, 4)
        self.layout.addWidget(self.s_slider, 8, 2, 1, 4)
        self.layout.addWidget(self.v_slider, 9, 2, 1, 4)
    
    def create_color_rectangle(self):
        self.rectangle = QFrame()
        self.rectangle.setFrameShape(QFrame.Box)
        self.rectangle.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.layout.addWidget(self.rectangle, 0, 6, 9, 5)
    
    def block_cmyk(self, val: bool):
        self.c_slider.blockSignals(val)
        self.m_slider.blockSignals(val)
        self.y_slider.blockSignals(val)
        self.k_slider.blockSignals(val)

    def block_rgb(self, val: bool):
        self.r_slider.blockSignals(val)
        self.g_slider.blockSignals(val)
        self.b_slider.blockSignals(val)

    def block_hsv(self, val: bool):
        self.h_slider.blockSignals(val)
        self.s_slider.blockSignals(val)
        self.v_slider.blockSignals(val)

    def update_ledits(self):
        self.c_ledit.setText(str(self.c))
        self.m_ledit.setText(str(self.m))
        self.y_ledit.setText(str(self.ys))
        self.k_ledit.setText(str(self.k))
        self.r_ledit.setText(str(self.r))
        self.g_ledit.setText(str(self.g))
        self.b_ledit.setText(str(self.b))
        self.h_ledit.setText(str(self.h))
        self.s_ledit.setText(str(self.s))
        self.v_ledit.setText(str(self.v))

    def update_from_cmyk(self):
        (self.r, self.g, self.b) = ColorConverter.cmyk_to_rgb(self.c, self.m, self.ys, self.k)
        (self.h, self.s, self.v) = ColorConverter.rgb_to_hsv(self.r, self.g, self.b)
        self.rectangle.setStyleSheet("background-color: rgb(" + str(int(self.r)) + ", "+str(int(self.g))+", " + str(int(self.b)) +");")
        self.update_ledits()
        self.block_rgb(True)
        self.block_hsv(True)
        self.r_slider.setValue(int(self.r))
        self.g_slider.setValue(int(self.g))
        self.b_slider.setValue(int(self.b))
        self.h_slider.setValue(int(self.h))
        self.s_slider.setValue(int(self.s))
        self.v_slider.setValue(int(self.v))
        self.block_rgb(False)
        self.block_hsv(False)

    def sup_update_ledit(self):
        self.update_ledits()
        self.block_rgb(True)
        self.block_hsv(True)
        self.block_cmyk(True)
        self.c_slider.setValue(int(self.c))
        self.m_slider.setValue(int(self.m))
        self.y_slider.setValue(int(self.ys))
        self.k_slider.setValue(int(self.k))
        self.r_slider.setValue(int(self.r))
        self.g_slider.setValue(int(self.g))
        self.b_slider.setValue(int(self.b))
        self.h_slider.setValue(int(self.h))
        self.s_slider.setValue(int(self.s))
        self.v_slider.setValue(int(self.v))
        self.block_cmyk(False)
        self.block_rgb(False)
        self.block_hsv(False)
        self.rectangle.setStyleSheet("background-color: rgb(" + str(int(self.r)) + ", "+str(int(self.g))+", " + str(int(self.b)) +");")

    def update_from_cmyk_ledit(self):
        (self.r, self.g, self.b) = ColorConverter.cmyk_to_rgb(self.c, self.m, self.ys, self.k)
        (self.h, self.s, self.v) = ColorConverter.rgb_to_hsv(self.r, self.g, self.b)
        self.sup_update_ledit()
    
    def update_from_rgb_ledit(self):
        (self.c, self.m, self.ys, self.k) = ColorConverter.rgb_to_cmyk(self.r, self.g, self.b)
        (self.h, self.s, self.v) = ColorConverter.rgb_to_hsv(self.r, self.g, self.b)
        self.sup_update_ledit()
        
    def update_from_hsv_ledit(self):
        (self.r, self.g, self.b) = ColorConverter.hsv_to_rgb(self.h, self.s, self.v)
        (self.c, self.m, self.ys, self.k) = ColorConverter.rgb_to_cmyk(self.r, self.g, self.b)
        self.sup_update_ledit()

    def update_from_rgb(self):
        (self.c, self.m, self.ys, self.k) = ColorConverter.rgb_to_cmyk(self.r, self.g, self.b)
        (self.h, self.s, self.v) = ColorConverter.rgb_to_hsv(self.r, self.g, self.b)
        self.rectangle.setStyleSheet("background-color: rgb(" + str(int(self.r)) + ", "+str(int(self.g))+", " + str(int(self.b)) +");")
        self.update_ledits()
        self.block_cmyk(True)
        self.block_hsv(True)
        self.c_slider.setValue(int(self.c))
        self.m_slider.setValue(int(self.m))
        self.y_slider.setValue(int(self.ys))
        self.k_slider.setValue(int(self.k))
        self.h_slider.setValue(int(self.h))
        self.s_slider.setValue(int(self.s))
        self.v_slider.setValue(int(self.v))
        self.block_cmyk(False)
        self.block_hsv(False)

    def update_from_hsv(self):
        (self.r, self.g, self.b) = ColorConverter.hsv_to_rgb(self.h, self.s, self.v)
        (self.c, self.m, self.ys, self.k) = ColorConverter.rgb_to_cmyk(self.r, self.g, self.b)
        self.rectangle.setStyleSheet("background-color: rgb(" + str(int(self.r)) + ", "+str(int(self.g))+", " + str(int(self.b)) +");")
        self.update_ledits()
        self.block_cmyk(True)
        self.block_rgb(True)
        self.c_slider.setValue(int(self.c))
        self.m_slider.setValue(int(self.m))
        self.y_slider.setValue(int(self.ys))
        self.k_slider.setValue(int(self.k))
        self.r_slider.setValue(int(self.r))
        self.g_slider.setValue(int(self.g))
        self.b_slider.setValue(int(self.b))
        self.block_cmyk(False)
        self.block_rgb(False)

    def on_c_ledit_change(self):
        self.c = int(self.c_ledit.text())
        self.update_from_cmyk_ledit()
    
    def on_m_ledit_change(self):
        self.m = int(self.m_ledit.text())
        self.update_from_cmyk_ledit()

    def on_y_ledit_change(self):
        self.ys = int(self.y_ledit.text())
        self.update_from_cmyk_ledit()

    def on_k_ledit_change(self):
        self.k = int(self.k_ledit.text())
        self.update_from_cmyk_ledit()

    def on_r_ledit_change(self):
        self.r = int(self.r_ledit.text())
        self.update_from_rgb_ledit()

    def on_g_ledit_change(self):
        self.g = int(self.g_ledit.text())
        self.update_from_rgb_ledit()

    def on_b_ledit_change(self):
        self.b = int(self.b_ledit.text())
        self.update_from_rgb_ledit()

    def on_h_ledit_change(self):
        self.h = int(self.h_ledit.text())
        self.update_from_hsv_ledit()

    def on_s_ledit_change(self):
        self.s = int(self.s_ledit.text())
        self.update_from_hsv_ledit()

    def on_v_ledit_change(self):
        self.v = int(self.v_ledit.text())
        self.update_from_hsv_ledit()

    def on_c_slider_change(self, value):
        self.c = int(value)
        self.update_from_cmyk()
    
    def on_m_slider_change(self, value):
        self.m = int(value)
        self.update_from_cmyk()

    def on_y_slider_change(self, value):
        self.ys = int(value)
        self.update_from_cmyk()

    def on_k_slider_change(self, value):
        self.k = int(value)
        self.update_from_cmyk()

    def on_r_slider_change(self, value):
        self.r = int(value)
        self.update_from_rgb()

    def on_g_slider_change(self, value):
        self.g = int(value)
        self.update_from_rgb()

    def on_b_slider_change(self, value):
        self.b = int(value)
        self.update_from_rgb()

    def on_h_slider_change(self, value):
        self.h = int(value)
        self.update_from_hsv()

    def on_s_slider_change(self, value):
        self.s = int(value)
        self.update_from_hsv()

    def on_v_slider_change(self, value):
        self.v = int(value)
        self.update_from_hsv()



def main():
    app = QApplication(sys.argv)
    window = SimpleApp()
    window.setWindowTitle("Lab1")
    window.setGeometry(100, 100, 400, 200)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
