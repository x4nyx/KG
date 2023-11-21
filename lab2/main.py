import sys
from PyQt5.QtWidgets import QApplication
from widgets.new_main_window import MainWindow


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("Lab 2")
    window.setGeometry(100, 100, 1200, 800)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
