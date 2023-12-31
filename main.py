import sys
import os
import pandas as pd
import numpy as np
import time
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QSizePolicy, QProgressBar, QMessageBox, QLabel
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtCore import QUrl
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtGui import QPixmap, QImage
from ui_test import Ui_Dialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib
from PIL import Image, ImageDraw
matplotlib.use('TkAgg')
import cv2
import json

class MainWindow(QMainWindow, Ui_Dialog) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        with open('config.json') as f:
            self.read_cf = json.load(f)
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.horizontalLayout.addWidget(self.canvas)
        self.video_widget = QVideoWidget()
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.video_widget)

        self.comBox.addItem("Point")
        self.comBox.addItem("Energy")
        self.comBox.addItem("Spectrum")
        self.comBox.setCurrentIndex(-1)
        self.comBox.currentIndexChanged.connect(self.update_comBox)
        self.comBox_2.currentIndexChanged.connect(self.update_comBox2)
        self.Pre_2.clicked.connect(self.PreProcess_Click)
        self.Exe.clicked.connect(self.View_Click)
        self.Stop.clicked.connect(self.Stop_Click)
        self.input_find.clicked.connect(self.input_path_find)
        self.save_find.clicked.connect(self.save_path_find)
        self.input_name = self.read_cf.get('input_dir')[0]
        if self.input_name == "":
            self.input_name = self.read_cf.get('default_dir')[0]
        self.save_name = self.read_cf.get('save_dir')[0]
        if self.save_name == "":
            self.save_name = self.read_cf.get('default_dir')[0]
        self.save_path.setText(self.save_name)
        self.input_path.setText(self.input_name)
        self.input_image_dir = self.input_name + "\\Far Pointing"
        self.input_energy_dir = self.input_name + "\\Energy"
        self.input_spectrum_dir = self.input_name + "\\Spectrum"
        self.input_temp_dir = self.input_name + "\\Temperature"
        self.warn_lb.setText("Data 전처리 필요")
        self.clear_para1 = 0
        self.clear_para2 = 0

    def save_config_json(self):
        with open('config.json', 'w') as f:
            json.dump(self.read_cf, f, indent=4)

    def input_path_find(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly  # Make the file read-only
        self.input_name = QFileDialog.getExistingDirectory(self, 'Open file', './', options=options)
        self.input_path.setText(self.input_name)
        self.input_image_dir = self.input_name + "\\Far Pointing"
        self.input_energy_dir = self.input_name + "\\Energy"
        self.input_spectrum_dir = self.input_name + "\\Spectrum"
        self.input_temp_dir = self.input_name + "\\Temperature"
        self.read_cf['input_dir'] = [self.input_name]
        self.save_config_json()
        self.warn_lb.setText("")

    def save_path_find(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly  # Make the file read-only
        self.save_name = QFileDialog.getExistingDirectory(self, 'Open file', './',  options=options)
        self.save_path.setText(self.save_name)
        self.read_cf['save_dir'] = [self.save_name]
        self.save_config_json()

    def update_comBox(self):
        self.comBox_2.clear()
        select_comBox = self.comBox.currentText()
        if select_comBox == "Point":
            self.clear_para1 = 1
            self.comBox_2.addItem("Point_XY")
            self.comBox_2.addItem("Point_Overlay")
            self.comBox_2.addItem("Point_Moving")
            self.comBox_2.setCurrentIndex(-1)
        elif select_comBox == "Energy":
            self.clear_para1 = 2
            self.comBox_2.addItem("Energy_Graph")
            self.comBox_2.setCurrentIndex(-1)
        elif select_comBox == "Spectrum":
            self.clear_para1 = 3
            self.comBox_2.addItem("Spectrum_Graph")
            self.comBox_2.setCurrentIndex(-1)

    def update_comBox2(self):
        select_comBox2 = self.comBox_2.currentText()
        self.GUI_clear()
        if select_comBox2 == "Point_XY":
            self.clear_para2 = 1
            self.horizontalLayout.addWidget(self.canvas)
        elif select_comBox2 == "Point_Overlay":
            self.clear_para2 = 2
        elif select_comBox2 == "Point_Moving":
            self.clear_para2 = 3
            self.video_widget = QVideoWidget()
            self.video_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.player = QMediaPlayer()
            self.player.setVideoOutput(self.video_widget)

            self.horizontalLayout.addWidget(self.video_widget)
            self.player.setSource(self.url)

    def PreProcess_Click(self):
        self.Point_Graph()
        self.videoplayer()
        self.warn_lb.setText("전처리 준비완료")

    def View_Click(self):
        select_comBox2 = self.comBox_2.currentText()
        if select_comBox2 == "Point_XY":
            self.XY_draw()
            self.canvas.mpl_connect('motion_notify_event', self.on_mouse_move)
            self.canvas.mpl_connect('button_press_event', self.on_mouse_click)
        elif select_comBox2 == "Point_Overlay":
            image = QImage(self.save_name + "\\overlay_image.png")
            pixmap = QPixmap.fromImage(image)
            self.Pix_label = QLabel()
            self.Pix_label.setPixmap(pixmap)
            self.Pix_label.setScaledContents(True)
            self.horizontalLayout.addWidget(self.Pix_label)
        elif select_comBox2 == "Point_Moving":
            self.video_btn.clicked.connect(self.player.play())
        elif select_comBox2 == "Energy_Graph":
            self.Energy_draw()
            self.canvas.mpl_connect('motion_notify_event', self.on_mouse_move)
            self.canvas.mpl_connect('button_press_event', self.on_mouse_click)
        elif select_comBox2 == "Spectrum_Graph":
            self.Spectrum_Graph()
            self.canvas.mpl_connect('motion_notify_event', self.on_mouse_move)
            self.canvas.mpl_connect('button_press_event', self.on_mouse_click)

    def Stop_Click(self):
        select_comBox2 = self.comBox_2.currentText()
        if select_comBox2 == "Point_XY":
            pass
        elif select_comBox2 == "Point_Overlay":
            pass
        elif select_comBox2 == "Point_Moving":
            self.player.pause()

    def Point_Graph(self):
        file_names = [f for f in os.listdir(self.input_image_dir) if f.endswith(".cam02.png")]
        # Initialize the total processing time
        total_processing_time = 0.0
        # Create a progress bar widget
        progress_bar = QProgressBar(self)
        progress_bar.setGeometry(30, 40, 200, 25)
        self.statusBar().addWidget(progress_bar)
        # ROI coordinates (left, upper, right, lower)
        roi_coordinates = (90, 170, 170, 270)
        # Create an empty DataFrame to store the average data
        self.average_data = pd.DataFrame(columns=['Date Saved', 'Average X', 'Average Y'])
        # Lists to store average X and Y data for plotting
        average_x_values = []
        average_y_values = []
        # Lists to store all average points
        all_average_points = []
        overlay_pixels = []
        for i, file_name in enumerate(file_names):
            # Construct the full file path
            file_path = os.path.join(self.input_image_dir, file_name)
            # Get the date the file was last modified
            date_saved = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(file_path)))
            # Open the PNG file
            image = Image.open(file_path)
            image = image.crop(roi_coordinates)
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
            top_20_pixels = top_pixels[:20]
            overlay_pixels = top_20_pixels
            # Calculate the average (x, y) data
            average_x = sum(x for x, _, _ in top_20_pixels) / len(top_20_pixels)
            average_y = sum(y for _, y, _ in top_20_pixels) / len(top_20_pixels)
            # Calculate the elapsed time for this image
            elapsed_time = time.time() - start_time
            progress_percentage = ((i + 1) / len(file_names)) * 100
            # Update the total processing time
            total_processing_time += elapsed_time
            # Append the date saved and average data to the DataFrame
            new_data = pd.DataFrame({'Date Saved': [date_saved], 'Average X': [average_x], 'Average Y': [average_y]})
            self.average_data = pd.concat([self.average_data, new_data], ignore_index=True)
            # Append average X and Y data for plotting
            average_x_values.append(average_x)
            average_y_values.append(average_y)
            # Append the average point to the list of all average points
            all_average_points.append((average_x, average_y))
            # Save the image with top 20 points highlighted
            top_image_path = os.path.join(self.save_name, f'top_20_image_{i}.png')
            new_image = Image.new('RGB', (width, height))
            draw = ImageDraw.Draw(new_image)
            for x, y, _ in top_20_pixels:
                draw.ellipse((x - 1, y - 1, x + 1, y + 1), fill=(255, 0, 0))  # Red dots
            new_image.save(top_image_path)
            # Update the progress bar
            progress_bar.setValue(progress_percentage)
            QApplication.processEvents()
        overlay_image = Image.new('RGB', (width, height))
        draw = ImageDraw.Draw(overlay_image)
        for x, y, _ in overlay_pixels:
            draw.ellipse((x - 1, y - 1, x + 1, y + 1), fill=(255, 0, 0))  # Red dots
        overlay_image.save(os.path.join(self.save_name, f'overlay_image.png'))
        # Clean up by removing the progress bar
        self.statusBar().removeWidget(progress_bar)
        progress_bar.deleteLater()
        self.average_data['Date Saved'] = pd.to_datetime(self.average_data['Date Saved'])

    def XY_draw(self):
        self.ax = self.figure.add_subplot(111)
        self.ax.plot(self.average_data['Date Saved'], self.average_data['Average X'], marker='o', markersize='3', linestyle='', label='Average X')
        self.ax.plot(self.average_data['Date Saved'], self.average_data['Average Y'], marker='s', markersize='3', linestyle='', label='Average Y')
        self.ax.legend(loc='center right', framealpha=0.5)
        self.ax.set_xlabel('Date Saved')
        self.ax.set_ylabel('Values')
        self.ax.set_title('Average X and Y Over Time')
        self.canvas.draw()

    def videoplayer(self):
        # Create a video from the image files with interpolation
        video_name = self.save_name + '//output_video.avi'
        frame_rate = 500  # Adjust the frame rate as needed
        # Frame interpolation factor (adjust for smoother or faster video)
        interpolation_factor = 10  # Increase for smoother video, decrease for faster video
        # Sort the image files to ensure they are in the correct order
        image_files = sorted([f for f in os.listdir(self.save_name) if f.startswith("top_20_image_")])
        # Get the dimensions of the first image (assuming all images have the same dimensions)
        first_image = Image.open(os.path.join(self.save_name, image_files[0]))
        width, height = first_image.size
        # Define the video codec
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        # Create the video writer
        video = cv2.VideoWriter(video_name, fourcc, frame_rate, (width, height))
        # Loop through the image files and add them to the video with interpolation
        for i in range(len(image_files) - 1):
            image_path1 = os.path.join(self.save_name, image_files[i])
            image_path2 = os.path.join(self.save_name, image_files[i + 1])
            # Open the images
            image1 = cv2.imread(image_path1)
            image2 = cv2.imread(image_path2)
            # Perform frame interpolation
            for j in range(interpolation_factor):
                alpha = j / interpolation_factor
                interpolated_frame = cv2.addWeighted(image1, 1 - alpha, image2, alpha, 0)
                video.write(interpolated_frame)
        # Release the video writer and close the video file
        video = video.release()
        self.url = QUrl.fromLocalFile(video_name)

    def Spectrum_Graph(self):
        self.figure.clear()
        file_names = [f for f in os.listdir(self.input_spectrum_dir) if f.startswith("Manual")]
        self.figure.subplots_adjust(hspace=0.5, wspace=0.5)
        for i, file_name in enumerate(file_names):
            # Construct the full file path
            file_path = os.path.join(self.input_spectrum_dir, file_name)
            data = pd.read_csv(file_path, delimiter='\t', encoding='utf-16')
            pl = self.figure.add_subplot(2,2,1+i)
            data = data.T
            for j in data.columns:
                label_text = data.iloc[0, j]
                data_time = label_text[:5]
                pl.plot(data.iloc[1:, j], label=data_time)
            pl.set_xlabel('Wavelength')
            pl.set_ylabel('Arbitrary Unit')
            x_ticks = pl.get_xticks()
            x_ticks = x_ticks[::500]
            pl.set_xticks(x_ticks)
            x_label = pl.get_xticklabels()
            new_tick_labels = [f"{int(label.get_text().split('.')[0])}" for label in x_label]
            pl.set_xticklabels(new_tick_labels)
            pl.legend(loc='upper left', framealpha=0.1)
            pl.set_title(file_name)
            self.canvas.draw()

    def Energy_draw(self):
        self.figure.clear()
        file_path = os.path.join(self.input_energy_dir, os.listdir(self.input_energy_dir)[0])
        data = pd.read_csv(file_path, delimiter='\t', encoding='utf-8')
        pl = self.figure.add_subplot(2, 2, 1)
        for i, column in enumerate(data.columns):
            if i == 1 or i == 2 or i == 3:
                pl.plot(data.iloc[1:,0],data.iloc[1:,i], label=column)
            else:
                pass
        pl.set_xlabel('Time')
        pl.set_ylabel('Power')
        x_ticks = pl.get_xticks()
        x_ticks = x_ticks[::500]
        pl.set_xticks(x_ticks)
        pl.legend(loc='upper left', framealpha=0.5)
        pl = self.figure.add_subplot(2, 2, 2)
        for i, column in enumerate(data.columns):
            if i == 4 or i == 5 or i == 6 or i == 7:
                pl.plot(data.iloc[1:, 0], data.iloc[1:, i], label=column)
            else:
                pass
        pl.set_xlabel('Time')
        pl.set_ylabel('Power')
        x_ticks = pl.get_xticks()
        x_ticks = x_ticks[::500]
        pl.set_xticks(x_ticks)
        pl.legend(loc='upper left', framealpha=0.5)
        pl = self.figure.add_subplot(2, 2, 3)
        for i, column in enumerate(data.columns):
            if i == 8 or i == 9 or i == 10:
                pl.plot(data.iloc[1:, 0], data.iloc[1:, i], label=column)
            else:
                pass
        pl.set_xlabel('Time')
        pl.set_ylabel('Power')
        x_ticks = pl.get_xticks()
        x_ticks = x_ticks[::500]
        pl.set_xticks(x_ticks)
        pl.legend(loc='upper left', framealpha=0.5)
        self.canvas.draw()

    def on_mouse_move(self, event):
        if event.inaxes:
            y = event.ydata
            if y is not None:
                coordinates_text = f'value={int(y)}'
                self.move_lb.setText(coordinates_text)

    def on_mouse_click(self, event):
        if event.button == 1:
            y = event.ydata
            if y is not None:
                coordinates_text = f'check={int(y)}'
                self.point_lb.setText(coordinates_text)

    def GUI_clear(self):
        self.point_lb.setText("")
        self.move_lb.setText("")
        if self.clear_para1 == 1 and self.clear_para2 == 1:
            self.figure.clear()
            self.canvas.draw()
            self.horizontalLayout.removeWidget(self.canvas)
        elif self.clear_para1 == 1 and self.clear_para2 == 2:
            self.horizontalLayout.removeWidget(self.Pix_label)
            self.Pix_label.setParent(None)
        elif self.clear_para1 == 1 and self.clear_para2 == 3:
            self.horizontalLayout.removeWidget(self.video_widget)
            self.video_widget.setParent(None)
        else:
            self.figure.clear()
            self.canvas.draw()
            self.horizontalLayout.removeWidget(self.canvas)

def error(message):
    error_box = QMessageBox()
    error_box.setIcon(QMessageBox.Critical)
    error_box.setText("An error occurred.")
    error_box.setInformativeText(message)
    error_box.setWindowTitle("Error")
    error_box.setStandardButtons(QMessageBox.Ok)
    error_box.exec()

# 차트범위 조절, thresold, roi조절

if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        main_win = MainWindow()
        main_win.show()
        sys.exit(app.exec())
    except Exception as e:
        error(str(e))
