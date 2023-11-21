from PyQt5.QtWidgets import QApplication, QListWidget, QFileDialog, QMainWindow, QGraphicsView, QGraphicsScene, QLabel, QPushButton, QGraphicsPixmapItem, QGridLayout, QWidget, QLineEdit
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt
from modules.image_converter import ImageConverter
import cv2
import os


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        
        self.layout = QGridLayout()
        self.setup_image_preview()
        self.setup_image_chooser()
        central_widget.setLayout(self.layout)

    def open_folder_chooser(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Выберите папку с изображениями")
        if folder_path:
            self.load_images(folder_path)

    def load_images(self, folder_path):
        self.image_list_chooser.clear()
        self.image_paths_chooser = []
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                    self.image_paths_chooser.append(os.path.join(root, file))
                    self.image_list_chooser.addItem(os.path.basename(file))


    def setup_image_chooser(self):
        self.image_list_chooser = QListWidget()
        self.image_list_chooser.itemClicked.connect(self.show_image)
        self.layout.addWidget(self.image_list_chooser, 0, 0)
        
        self.image_preview_chooser = QGraphicsView()
        self.image_preview_chooser.setScene(QGraphicsScene())
        self.layout.addWidget(self.image_preview_chooser, 0, 1)
        
        self.open_button_chooser = QPushButton("Открыть папку")
        self.open_button_chooser.setFont(QFont('Arial', 12))
        self.open_button_chooser.clicked.connect(self.open_folder_chooser)
        self.layout.addWidget(self.open_button_chooser, 1, 0)

        self.preview_label = QLabel('Исходное изображение')
        self.preview_label.setFont(QFont('Arial', 14))
        self.layout.addWidget(self.preview_label, 1, 1)

    def setup_image_preview(self):
        self.image_smooth_preview = QGraphicsView()
        self.image_smooth_preview.setScene(QGraphicsScene())
        self.image_gist_preview = QGraphicsView()
        self.image_gist_preview.setScene(QGraphicsScene())
        self.image_linear_preview = QGraphicsView()
        self.image_linear_preview.setScene(QGraphicsScene())
        self.image_smooth_label = QLabel('Сглаживающий фильтр')
        self.image_gist_label = QLabel('Эквализация гистограммы')
        self.image_linear_label = QLabel('Линейное контрастирование')
        font = QFont('Arial', 14)
        self.image_smooth_label.setFont(font)
        self.image_gist_label.setFont(font)
        self.image_linear_label.setFont(font)
        self.layout.addWidget(self.image_gist_preview, 2, 2)
        self.layout.addWidget(self.image_gist_label, 3, 2)
        self.layout.addWidget(self.image_linear_preview, 2, 1)
        self.layout.addWidget(self.image_linear_label, 3, 1)
        self.layout.addWidget(self.image_smooth_preview, 2, 0)
        self.layout.addWidget(self.image_smooth_label, 3, 0)


    def config_paths(self, image_path):
        self.folder_path = os.path.dirname(image_path)
        self.parent_folder_path = os.path.abspath(os.path.join(self.folder_path, os.pardir))
        self.temp_folder_path = self.parent_folder_path + '/temporary'
        if not os.path.isdir(self.temp_folder_path):
            os.mkdir(self.temp_folder_path)
        self.smooth_path = self.temp_folder_path + '/smooth.png'
        self.gist_path = self.temp_folder_path + '/gist.png'
        self.linear_path = self.temp_folder_path + '/linear.png'

    def smooth_image(self):
        smooth_scene = self.image_smooth_preview.scene()
        smooth_scene.clear()
        
        image = cv2.imread(self.image_path)
        image = ImageConverter.cv_homogeneous_avg_filter(image, (5, 5))
        cv2.imwrite(self.smooth_path, image)

        smooth_pixmap = QPixmap(self.smooth_path)

        smooth_max_width = self.image_smooth_preview.width()
        smooth_max_height = self.image_smooth_preview.height()
        smooth_pixmap = smooth_pixmap.scaled(smooth_max_width, smooth_max_height, Qt.KeepAspectRatio)
        smooth_scene.addItem(QGraphicsPixmapItem(smooth_pixmap))
    
    def gist_image(self):
        gist_scene = self.image_gist_preview.scene()
        gist_scene.clear()
        
        image = cv2.imread(self.image_path)
        image = ImageConverter.equalize(image)
        
        cv2.imwrite(self.gist_path, image)

        gist_pixmap = QPixmap(self.gist_path)

        gist_max_width = self.image_gist_preview.width()
        gist_max_height = self.image_gist_preview.height()
        gist_pixmap = gist_pixmap.scaled(gist_max_width, gist_max_height, Qt.KeepAspectRatio)
        gist_scene.addItem(QGraphicsPixmapItem(gist_pixmap))

    def linear_image(self):
        linear_scene = self.image_linear_preview.scene()
        linear_scene.clear()
        
        image = cv2.imread(self.image_path)
        image = ImageConverter.linear_filter(image)
        cv2.imwrite(self.linear_path, image)

        linear_pixmap = QPixmap(self.linear_path)

        linear_max_width = self.image_linear_preview.width()
        linear_max_height = self.image_linear_preview.height()
        linear_pixmap = linear_pixmap.scaled(linear_max_width, linear_max_height, Qt.KeepAspectRatio)
        linear_scene.addItem(QGraphicsPixmapItem(linear_pixmap))

    def show_image(self, item):
        selected_item = self.image_list_chooser.currentRow()
        if selected_item >= 0:
            self.image_path = self.image_paths_chooser[selected_item]
            self.config_paths(self.image_path)
            pixmap = QPixmap(self.image_path)
            scene = self.image_preview_chooser.scene()
            scene.clear()
            pixmap = QPixmap(self.image_path)
            self.smooth_image()
            self.gist_image()
            self.linear_image()

            max_width = self.image_preview_chooser.width()
            max_height = self.image_preview_chooser.height()
            
            pixmap = pixmap.scaled(max_width, max_height, Qt.KeepAspectRatio)
            scene.addItem(QGraphicsPixmapItem(pixmap))

    

    
