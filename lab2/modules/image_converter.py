from PyQt5.QtGui import QPixmap, QImage
import cv2
import numpy as np
import matplotlib.pyplot as plt

class ImageConverter:
    @staticmethod
    def from_pixmap_to_cv(pixmap: QPixmap):
        image = pixmap.toImage()
        width, height = image.width(), image.height()
        ptr = image.bits()
        ptr.setsize(image.byteCount())
        arr = np.array(ptr).reshape(height, width, 4)  # 4 channels (RGBA)

        # 3. Convert the NumPy array to an OpenCV image
        opencv_image = cv2.cvtColor(arr, cv2.COLOR_RGB2BGR)
        return opencv_image
        

    @staticmethod
    def from_cv_to_pixmap(np_img):
        frame = cv2.cvtColor(np_img, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        return QPixmap.fromImage(img)
    
    @staticmethod
    def homogeneous_avg_filter(pixmap: QPixmap, kernel_size):
        image_cv = ImageConverter.from_pixmap_to_cv(pixmap)
        #smoothed_image = cv2.GaussianBlur(image_cv, kernel_size, 0)
        return ImageConverter.from_cv_to_pixmap(image_cv)

    @staticmethod
    def cv_homogeneous_avg_filter(image_cv, kernel_size):
        smoothed_image = cv2.GaussianBlur(image_cv, kernel_size, 0)
        return smoothed_image

    @staticmethod
    def gauss_filter(image_cv, kernel_size):
        smoothed_image = cv2.GaussianBlur(image_cv, kernel_size, 0)
        return smoothed_image
    
    @staticmethod
    def equalize(image_cv):
        image_cv = cv2.cvtColor(image_cv, cv2.COLOR_BGR2GRAY)

        equalized_img = cv2.equalizeHist(image_cv)

        hist1 = cv2.calcHist([image_cv], [0], None, [256], [0, 256])
        hist2 = cv2.calcHist([equalized_img], [0], None, [256], [0, 256]) 
        
        plt.figure(figsize=(12, 6))

        plt.subplot(1, 2, 1)
        plt.plot(hist1, color='blue')
        plt.title('Original image')
        plt.xlabel('Pixel Value')
        plt.ylabel('Frequency')

        plt.subplot(1, 2, 2)
        plt.plot(hist2, color='blue')
        plt.title('Equlized image')
        plt.xlabel('Pixel Value')
        plt.ylabel('Frequency')

        plt.show()
        return equalized_img
    
    @staticmethod
    def linear_filter(image_cv):
        gray_img = cv2.cvtColor(image_cv, cv2.COLOR_BGR2GRAY)
        min_val, max_val, _, _ = cv2.minMaxLoc(gray_img)
        alpha = 255 / (max_val - min_val)
        beta = -min_val * alpha
        linear_contrast_img = cv2.convertScaleAbs(gray_img, alpha=alpha, beta=beta)
        return linear_contrast_img
