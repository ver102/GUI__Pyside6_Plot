import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QHBoxLayout, QWidget, QSizePolicy
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class ImageDisplayApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Display Example")
        self.setGeometry(100, 100, 600, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create a horizontal layout
        layout = QHBoxLayout(central_widget)

        # Load an image from a file
        image_path = "C:\\Users\\USER\\Desktop\\20220803\\save\\overlay_image.png"  # Replace with the path to your image file
        image = QPixmap(image_path)

        if not image.isNull():
            label = QLabel()
            label.setPixmap(image)
            label.setAlignment(Qt.AlignCenter)  # Center the image in the label

            # Set the size policy to expand and the aspect ratio policy
            label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            label.setScaledContents(True)

            # Add the label to the layout
            layout.addWidget(label)
        else:
            # Handle the case where the image couldn't be loaded
            label = QLabel("Image not found")
            layout.addWidget(label)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageDisplayApp()
    window.show()
    sys.exit(app.exec_())
