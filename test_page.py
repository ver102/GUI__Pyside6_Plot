import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QFileDialog, QSizePolicy, QProgressBar
from PySide6.QtCore import QUrl, Qt, QTimer
from ui_test import Ui_Dialog
import json
import threading  # Import the threading module
from Far_Point_class import PointSeparator
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib

matplotlib.use('Qt5Agg')  # Use Qt5Agg backend

class MainWindow(QMainWindow, Ui_Dialog):

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
            # Create a separate thread to perform the time-consuming task
            def run_point_separation():
                point_sep = PointSeparator(self.input_image_dir)
                point_sep.process()
                average_data = point_sep.average_dat

                # Update the UI with the result (use Qt's signal/slot mechanism)

                # Define a slot function to update the UI
                def update_ui():
                    self.figure.clear()
                    self.canvas.draw()
                    self.ax = self.figure.add_subplot(111)
                    # Plot average_x and average_y as markers without lines
                    self.ax.plot(average_data['Date Saved'], average_data['Average X'], marker='o', linestyle='',
                                 label='Average X')
                    self.ax.plot(average_data['Date Saved'], average_data['Average Y'], marker='s', linestyle='',
                                 label='Average Y')
                    # Set labels and title
                    self.ax.set_xlabel('Date Saved')
                    self.ax.set_ylabel('Values')
                    self.ax.set_title('Average X and Y Over Time')
                    # Add a legend
                    self.canvas.draw()

                # Execute the slot function in the main (UI) thread
                self.canvas.draw()
                QTimer.singleShot(0, update_ui)

            # Create and start the thread
            self.worker_thread = threading.Thread(target=run_point_separation)
            self.worker_thread.start()
        elif select_comBox2 == "Point_XY_Garph":
            self.label.setText("진행중2")
        elif select_comBox2 == "Point_Moving":
            self.label.setText("진행중3")

        self.canvas.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
