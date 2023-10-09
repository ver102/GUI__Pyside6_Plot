import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QFileDialog, QSizePolicy, QProgressBar
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtCore import QUrl
from PySide6.QtGui import QIcon
from ui_test import Ui_Dialog
import os
from PIL import Image, ImageDraw
import numpy as np
import time
import pandas as pd
import matplotlib.cm as cm
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib
matplotlib.use('TkAgg')
import cv2
from datetime import datetime
import json

from Far_Point_class import *


#화면을 띄우는데 사용되는 Class 선언
class MainWindow(QMainWindow, Ui_Dialog) :
    def __init__(self) :
        super().__init__()

        self.setupUi(self)

        with open('test.json') as f:
            self.read_cf = json.load(f)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.verticalLayout_3.addWidget(self.canvas)

        self.comBox.addItem("Point")
        self.comBox.addItem("Energy")
        self.comBox.addItem("Spectrum")
        self.comBox.addItem("Temperature")
        self.comBox.setCurrentIndex(-1)
        self.comBox.currentIndexChanged.connect(self.update_comBox)
        self.comBox_2.currentIndexChanged.connect(self.Point_func)

        self.Exe.clicked.connect(self.Exe_Click)

        self.input_find.clicked.connect(self.input_path_find)
        self.save_find.clicked.connect(self.save_path_find)
        self.input_dir = self.read_cf.get('input_dir',[])
        self.save_dir = self.read_cf.get('save_dir',[])
        self.input_name = self.input_dir[0] if self.input_dir=="" else self.read_cf.get('default_path',[])[0]
        self.save_name = self.save_dir[0] if self.save_dir=="" else self.read_cf.get('default_path',[])[0]

        self.save_path.setText(self.save_name)
        self.input_path.setText(self.input_name)

        self.input_image_dir = self.input_name + "\\Far Pointing"
        self.input_energy_dir = self.input_name + "\\Energy"
        self.input_spectrum_dir = self.input_name + "\\Sepctrum"
        self.input_temp_dir = self.input_name + "\\Temperature"

    def save_config_to_json(self):
        with open('test.json', 'w') as f:
            json.dump(self.read_cf, f, indent=4)

    def input_path_find(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly  # Make the file read-only
        self.input_name = QFileDialog.getExistingDirectory(self, 'Open file', './', options=options)
        self.input_path.setText(self.input_name)
        self.input_image_dir = self.input_name + "\\Far Pointing"
        self.input_energy_dir = self.input_name + "\\Energy"
        self.input_spectrum_dir = self.input_name + "\\Sepctrum"
        self.input_temp_dir = self.input_name + "\\Temperature"
        self.read_cf['input_dir'] = [self.input_name]
        self.save_config_to_json()

    def save_path_find(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly  # Make the file read-only
        self.save_name= QFileDialog.getExistingDirectory(self, 'Open file', './',  options=options)
        self.save_path.setText(self.save_name)
        self.read_cf['save_dir'] = [self.save_name]
        self.save_config_to_json()

    def update_comBox(self):
        self.comBox_2.clear()
        select_comBox = self.comBox.currentText()
        if select_comBox == "Point":
            self.comBox_2.addItem("Point_Seperation")
            self.comBox_2.addItem("Point_XY_Garph")
            self.comBox_2.addItem("Point_Moving")
            self.comBox_2.setCurrentIndex(-1)
        elif select_comBox == "Energy":
            self.comBox_2.addItem("Energy_avg")
            self.comBox_2.addItem("Energy_std")
            self.comBox_2.setCurrentIndex(-1)
        elif select_comBox == "Spectrum":
            self.comBox_2.addItem("Spectrum_avg")
            self.comBox_2.addItem("Spectrum_std")
            self.comBox_2.setCurrentIndex(-1)
        elif select_comBox == "Temperature":
            self.comBox_2.addItem("Temperature_avg")
            self.comBox_2.addItem("Temperature_std")
            self.comBox_2.setCurrentIndex(-1)

    def Point_func(self):
        self.figure.clear()
        select_comBox2 = self.comBox_2.currentText()
        self.label.clear()
        self.label_2.clear()

    def Exe_Click(self):
        select_comBox2 = self.comBox_2.currentText()
        if select_comBox2 == "Point_Seperation":
            self.Point_Sep()
        elif select_comBox2 == "Point_XY_Garph":
            self.label.setText("진행중2")
        elif select_comBox2 == "Point_Moving":
            self.label.setText("진행중3")
        self.canvas.draw()

    def Point_Sep(self):
        self.figure.clear()
        self.canvas.draw()
        self.label.setText("자료 road 필요")
        self.label_2.setText("-")
        file_names = [f for f in os.listdir(self.input_image_dir) if f.endswith(".cam02.png")]
        # Initialize the total processing time
        total_processing_time = 0.0
        # Create a progress bar widget
        progress_bar = QProgressBar(self)
        progress_bar.setGeometry(30, 40, 200, 25)
        self.statusBar().addWidget(progress_bar)

        # Frame interpolation factor (adjust for smoother or faster video)
        interpolation_factor = 10  # Increase for smoother video, decrease for faster video

        # ROI coordinates (left, upper, right, lower)
        roi_coordinates = (70, 170, 180, 270)

        # Create an empty DataFrame to store the average data
        average_data = pd.DataFrame(columns=['Date Saved', 'Average X', 'Average Y'])

        # Lists to store average X and Y data for plotting
        average_x_values = []
        average_y_values = []

        # Lists to store all average points
        all_average_points = []

        # Lists to store colors for the legend in average_data_plot
        legend_colors = []

        # Process each ".cam02.png" file in the folder
        for i, file_name in enumerate(file_names):
            # Construct the full file path
            file_path = os.path.join(self.input_image_dir, file_name)

            # Get the date the file was last modified
            date_saved = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(file_path)))

            # Open the PNG file
            image = Image.open(file_path)

            # Convert the image to a NumPy array for faster processing
            image_array = np.array(image)

            # Define a threshold to filter out noisy pixels
            threshold = 1000  # Adjust this threshold as needed

            # Create a list to store the top 20 significant pixel values and their coordinates
            top_pixels = []

            # Get the dimensions of the image
            height, width = image_array.shape

            # Measure the start time
            start_time = time.time()

            # Iterate through all (x, y) coordinates and check pixel values
            for x in range(width):
                for y in range(height):
                    pixel_value = image_array[y, x]  # Get the pixel value (grayscale)
                    if pixel_value > threshold:
                        top_pixels.append((x, y, pixel_value))

            # Sort the list by pixel values in descending order
            top_pixels.sort(key=lambda x: x[2], reverse=True)

            # Get the top 20 pixel values and their coordinates
            top_20_pixels = top_pixels[:30]

            # Calculate the average (x, y) data
            average_x = sum(x for x, _, _ in top_20_pixels) / len(top_20_pixels)
            average_y = sum(y for _, y, _ in top_20_pixels) / len(top_20_pixels)

            # Calculate the elapsed time for this image
            elapsed_time = time.time() - start_time

            # Print the progress as a percentage
            progress_percentage = ((i + 1) / len(file_names)) * 100

            # Update the total processing time
            total_processing_time += elapsed_time

            # Append the date saved and average data to the DataFrame
            new_data = pd.DataFrame({'Date Saved': [date_saved], 'Average X': [average_x], 'Average Y': [average_y]})
            average_data = pd.concat([average_data, new_data], ignore_index=True)

            # Append average X and Y data for plotting
            average_x_values.append(average_x)
            average_y_values.append(average_y)

            # Append the average point to the list of all average points
            all_average_points.append((average_x, average_y))

            # Append a color to the legend_colors list for average_data_plot
            legend_colors.append(cm.plasma(i / len(file_names)))

            # Save the image with top 20 points highlighted
            top_points_image_path = os.path.join(self.input_image_dir, f'top_20_points_image_{i}.png')
            new_image = Image.new('RGB', (width, height))
            draw = ImageDraw.Draw(new_image)
            for x, y, _ in top_20_pixels:
                draw.ellipse((x - 1, y - 1, x + 1, y + 1), fill=(255, 0, 0))  # Red dots
            new_image.save(top_points_image_path)

            # Update the progress bar
            progress_bar.setValue(progress_percentage)
            QApplication.processEvents()

        # Clean up by removing the progress bar
        self.statusBar().removeWidget(progress_bar)
        progress_bar.deleteLater()
        # Convert 'Date Saved' to datetime format
        average_data['Date Saved'] = pd.to_datetime(average_data['Date Saved'])


        self.ax = self.figure.add_subplot(111)
        # Plot average_x and average_y as markers without lines
        self.ax.plot(average_data['Date Saved'], average_data['Average X'], marker='o', linestyle='', label='Average X')
        self.ax.plot(average_data['Date Saved'], average_data['Average Y'], marker='s', linestyle='', label='Average Y')
        # Set labels and title
        self.ax.set_xlabel('Date Saved')
        self.ax.set_ylabel('Values')
        self.ax.set_title('Average X and Y Over Time')
        # Add a legend
        self.canvas.draw()

"""
        try:
            age = int(input("나이를 입력하세요: "))  # 정수로 변환 시도
        except ValueError:
            print("올바른 파일이 아닙니다.")
        else:
            if age >= 18:
                print("성인입니다.")
            else:
                print("미성년자입니다.")



        self._video_widget = QVideoWidget()
        self._player = QMediaPlayer()

        self._player.setVideoOutput(self._video_widget)
        self.verticalLayout_4.addWidget(self._video_widget)

        url = QUrl.fromLocalFile('C:\\Users\\USER\\Desktop\waterfall_-_37088 (720p).mp4')
        self._player.setSource(url)
        self._player.play()
"""
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
#    available_geometry = main_win.screen().availableGeometry()
#    main_win.resize(available_geometry.width() / 3,
#                    available_geometry.height() / 2)
    main_win.show()
    sys.exit(app.exec())

