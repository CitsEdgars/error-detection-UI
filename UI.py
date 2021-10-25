from PyQt5 import QtCore, QtWidgets
import pyqtgraph as pg
from random import randint
from Fourier_analysis import get_simple_graph
import CRC as crc
import Hamming_code as hc
import numpy as np
from datetime import datetime
import math

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1029, 631)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1029, 631))
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName("tabWidget")
        self.hamming_tab = QtWidgets.QWidget()
        self.hamming_tab.setObjectName("hamming_tab")
        self.h_input = QtWidgets.QTextEdit(self.hamming_tab)
        self.h_input.setGeometry(QtCore.QRect(10, 30, 291, 131))
        self.h_input.setObjectName("h_input")
        self.h_input_label = QtWidgets.QLabel(self.hamming_tab)
        self.h_input_label.setGeometry(QtCore.QRect(10, 10, 101, 16))
        self.h_input_label.setObjectName("h_input_label")
        self.h_shock_dial = QtWidgets.QDial(self.hamming_tab)
        self.h_shock_dial.setGeometry(QtCore.QRect(430, 170, 71, 71))
        self.h_shock_dial.setObjectName("h_shock_dial")
        self.h_shocked_bits = QtWidgets.QLabel(self.hamming_tab)
        self.h_shocked_bits.setGeometry(QtCore.QRect(350, 170, 81, 71))
        self.h_shocked_bits.setObjectName("h_shocked_bits")
        self.h_chance_label = QtWidgets.QLabel(self.hamming_tab)
        self.h_chance_label.setGeometry(QtCore.QRect(180, 170, 91, 71))
        self.h_chance_label.setObjectName("h_chance_label")
        self.h_speed_slider = QtWidgets.QSlider(self.hamming_tab)
        self.h_speed_slider.setGeometry(QtCore.QRect(80, 550, 160, 22))
        self.h_speed_slider.setOrientation(QtCore.Qt.Horizontal)
        self.h_speed_slider.setObjectName("h_speed_slider")
        self.h_noise_label = QtWidgets.QLabel(self.hamming_tab)
        self.h_noise_label.setGeometry(QtCore.QRect(20, 170, 71, 71))
        self.h_noise_label.setObjectName("h_noise_label")
        self.h_pause_button = QtWidgets.QPushButton(self.hamming_tab)
        self.h_pause_button.setGeometry(QtCore.QRect(630, 540, 121, 41))
        self.h_pause_button.setObjectName("h_pause_button")
        self.h_noise_dial = QtWidgets.QDial(self.hamming_tab)
        self.h_noise_dial.setGeometry(QtCore.QRect(90, 170, 71, 71))
        self.h_noise_dial.setObjectName("h_noise_level_dial")
        self.h_chance_dial = QtWidgets.QDial(self.hamming_tab)
        self.h_chance_dial.setGeometry(QtCore.QRect(270, 170, 71, 71))
        self.h_chance_dial.setObjectName("h_shock_chance_dial")
        self.h_speed_label = QtWidgets.QLabel(self.hamming_tab)
        self.h_speed_label.setGeometry(QtCore.QRect(30, 550, 31, 21))
        self.h_speed_label.setObjectName("h_speed_label")
        self.h_send_button = QtWidgets.QPushButton(self.hamming_tab)
        self.h_send_button.setGeometry(QtCore.QRect(320, 120, 181, 41))
        self.h_send_button.setObjectName("h_send_button")
        self.h_continue_button = QtWidgets.QPushButton(self.hamming_tab)
        self.h_continue_button.setGeometry(QtCore.QRect(760, 540, 121, 41))
        self.h_continue_button.setObjectName("h_continue_button")
        self.h_exit_button = QtWidgets.QPushButton(self.hamming_tab)
        self.h_exit_button.setGeometry(QtCore.QRect(890, 540, 121, 41))
        self.h_exit_button.setObjectName("h_exit_button")
        self.h_received_log = QtWidgets.QTextEdit(self.hamming_tab)
        self.h_received_log.setGeometry(QtCore.QRect(520, 30, 491, 211))
        self.h_received_log.setObjectName("h_received_log")
        self.h_received_label = QtWidgets.QLabel(self.hamming_tab)
        self.h_received_label.setGeometry(QtCore.QRect(520, 10, 131, 16))
        self.h_received_label.setObjectName("h_received_label")
        self.h_frequency = QtWidgets.QComboBox(self.hamming_tab)
        self.h_frequency.setGeometry(QtCore.QRect(390, 60, 111, 22))
        self.h_frequency.setObjectName("h_frequency")
        self.h_level_label = QtWidgets.QLabel(self.hamming_tab)
        self.h_level_label.setGeometry(QtCore.QRect(320, 90, 71, 21))
        self.h_level_label.setObjectName("h_level_label")
        self.h_freq_label = QtWidgets.QLabel(self.hamming_tab)
        self.h_freq_label.setGeometry(QtCore.QRect(320, 60, 71, 21))
        self.h_freq_label.setObjectName("h_freq_label")
        self.h_sample_label = QtWidgets.QLabel(self.hamming_tab)
        self.h_sample_label.setGeometry(QtCore.QRect(320, 30, 61, 20))
        self.h_sample_label.setObjectName("h_sample_label")
        self.h_signal_levels = QtWidgets.QSpinBox(self.hamming_tab)
        self.h_signal_levels.setGeometry(QtCore.QRect(390, 90, 111, 22))
        self.h_signal_levels.setObjectName("h_signal_levels")
        self.h_sample_rate = QtWidgets.QComboBox(self.hamming_tab)
        self.h_sample_rate.setGeometry(QtCore.QRect(390, 30, 111, 22))
        self.h_sample_rate.setObjectName("h_sample_rate")
        self.tabWidget.addTab(self.hamming_tab, "")
        self.crc_tab = QtWidgets.QWidget()
        self.crc_tab.setObjectName("crc_tab")
        self.c_input = QtWidgets.QTextEdit(self.crc_tab)
        self.c_input.setGeometry(QtCore.QRect(10, 30, 431, 61))
        self.c_input.setObjectName("c_input")
        self.c_input_dial = QtWidgets.QLabel(self.crc_tab)
        self.c_input_dial.setGeometry(QtCore.QRect(10, 10, 101, 16))
        self.c_input_dial.setObjectName("c_input_dial")
        self.c_crc_combo = QtWidgets.QComboBox(self.crc_tab)
        self.c_crc_combo.setGeometry(QtCore.QRect(90, 100, 81, 22))
        self.c_crc_combo.setObjectName("c_crc_combo")
        self.c_crc_polynomial = QtWidgets.QLabel(self.crc_tab)
        self.c_crc_polynomial.setGeometry(QtCore.QRect(10, 100, 81, 21))
        self.c_crc_polynomial.setObjectName("c_crc_polynomial")
        self.c_coeffs = QtWidgets.QLineEdit(self.crc_tab)
        self.c_coeffs.setGeometry(QtCore.QRect(222, 100, 221, 51))
        self.c_coeffs.setObjectName("c_coeffs")
        self.c_coeffs_label = QtWidgets.QLabel(self.crc_tab)
        self.c_coeffs_label.setGeometry(QtCore.QRect(180, 100, 41, 51))
        self.c_coeffs_label.setObjectName("c_coeffs_label")
        self.c_send_button = QtWidgets.QPushButton(self.crc_tab)
        self.c_send_button.setGeometry(QtCore.QRect(450, 30, 51, 121))
        self.c_send_button.setObjectName("c_send_button")
        self.c_log = QtWidgets.QTextEdit(self.crc_tab)
        self.c_log.setGeometry(QtCore.QRect(520, 30, 491, 211))
        self.c_log.setObjectName("c_log")
        self.c_log_label = QtWidgets.QLabel(self.crc_tab)
        self.c_log_label.setGeometry(QtCore.QRect(520, 10, 131, 16))
        self.c_log_label.setObjectName("c_log_label")
        self.c_custom_poly = QtWidgets.QRadioButton(self.crc_tab)
        self.c_custom_poly.setGeometry(QtCore.QRect(10, 130, 161, 17))
        self.c_custom_poly.setObjectName("c_custom_poly")
        self.c_pause_button = QtWidgets.QPushButton(self.crc_tab)
        self.c_pause_button.setGeometry(QtCore.QRect(630, 540, 121, 41))
        self.c_pause_button.setObjectName("c_pause_button")
        self.c_continue_button = QtWidgets.QPushButton(self.crc_tab)
        self.c_continue_button.setGeometry(QtCore.QRect(760, 540, 121, 41))
        self.c_continue_button.setObjectName("c_continue_button")
        self.c_exit_button = QtWidgets.QPushButton(self.crc_tab)
        self.c_exit_button.setGeometry(QtCore.QRect(890, 540, 121, 41))
        self.c_exit_button.setObjectName("c_exit_button")
        self.c_speed_slider = QtWidgets.QSlider(self.crc_tab)
        self.c_speed_slider.setGeometry(QtCore.QRect(80, 550, 160, 22))
        self.c_speed_slider.setOrientation(QtCore.Qt.Horizontal)
        self.c_speed_slider.setObjectName("c_speed_dial")
        self.c_speed_label = QtWidgets.QLabel(self.crc_tab)
        self.c_speed_label.setGeometry(QtCore.QRect(30, 550, 31, 21))
        self.c_speed_label.setObjectName("c_speed_label")
        self.c_noise_dial = QtWidgets.QDial(self.crc_tab)
        self.c_noise_dial.setGeometry(QtCore.QRect(90, 170, 71, 71))
        self.c_noise_dial.setObjectName("c_noise_dial")
        self.c_noise_label = QtWidgets.QLabel(self.crc_tab)
        self.c_noise_label.setGeometry(QtCore.QRect(20, 170, 71, 71))
        self.c_noise_label.setObjectName("c_noise_label")
        self.c_chance_label = QtWidgets.QLabel(self.crc_tab)
        self.c_chance_label.setGeometry(QtCore.QRect(180, 170, 91, 71))
        self.c_chance_label.setObjectName("c_chance_label")
        self.c_chance_dial = QtWidgets.QDial(self.crc_tab)
        self.c_chance_dial.setGeometry(QtCore.QRect(270, 170, 71, 71))
        self.c_chance_dial.setObjectName("c_chance_dial")
        self.c_shocked_bits = QtWidgets.QLabel(self.crc_tab)
        self.c_shocked_bits.setGeometry(QtCore.QRect(350, 170, 81, 71))
        self.c_shocked_bits.setObjectName("c_shocked_bits")
        self.c_shock_dial = QtWidgets.QDial(self.crc_tab)
        self.c_shock_dial.setGeometry(QtCore.QRect(430, 170, 71, 71))
        self.c_shock_dial.setObjectName("c_shock_dial")
        self.tabWidget.addTab(self.crc_tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #My addition
        self.c_graphWidget = pg.PlotWidget(self.crc_tab)
        self.c_graphWidget.setGeometry(QtCore.QRect(10, 260, 1001, 271))
        self.c_graphWidget.setObjectName("graphWidget")
        self.c_graphWidget.aspectLocked.as_integer_ratio()

        self.h_graphWidget = pg.PlotWidget(self.hamming_tab)
        self.h_graphWidget.setGeometry(QtCore.QRect(10, 260, 1001, 271))
        self.h_graphWidget.setObjectName("graphWidget")
        self.h_graphWidget.aspectLocked.as_integer_ratio()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.h_input_label.setText(_translate("MainWindow", "Information to send"))
        self.h_shocked_bits.setText(_translate("MainWindow", "Shocked bits: 0"))
        self.h_chance_label.setText(_translate("MainWindow", "Shock chance: 0"))
        self.h_noise_label.setText(_translate("MainWindow", "Noise level: 0"))
        self.h_pause_button.setText(_translate("MainWindow", "Pause"))
        self.h_speed_label.setText(_translate("MainWindow", "Speed"))
        self.h_send_button.setText(_translate("MainWindow", "Send"))
        self.h_continue_button.setText(_translate("MainWindow", "Continue"))
        self.h_exit_button.setText(_translate("MainWindow", "Exit"))
        self.h_received_label.setText(_translate("MainWindow", "Received information logs"))
        self.h_level_label.setText(_translate("MainWindow", "Signal levels:"))
        self.h_freq_label.setText(_translate("MainWindow", "Frequency"))
        self.h_sample_label.setText(_translate("MainWindow", "Sample rate: "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.hamming_tab), _translate("MainWindow", "Hamming"))
        self.c_input_dial.setText(_translate("MainWindow", "Information to send"))
        self.c_crc_polynomial.setText(_translate("MainWindow", "CRC polynomial"))
        self.c_coeffs_label.setText(_translate("MainWindow", "Coeffs:"))
        self.c_send_button.setText(_translate("MainWindow", "Send"))
        self.c_log_label.setText(_translate("MainWindow", "Received information logs"))
        self.c_custom_poly.setText(_translate("MainWindow", "Use custom CRC polynomial"))
        self.c_pause_button.setText(_translate("MainWindow", "Pause"))
        self.c_continue_button.setText(_translate("MainWindow", "Continue"))
        self.c_exit_button.setText(_translate("MainWindow", "Exit"))
        self.c_speed_label.setText(_translate("MainWindow", "Speed"))
        self.c_noise_label.setText(_translate("MainWindow", "Noise level: 0"))
        self.c_chance_label.setText(_translate("MainWindow", "Shock chance: 0"))
        self.c_shocked_bits.setText(_translate("MainWindow", "Shocked bits: 0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.crc_tab), _translate("MainWindow", "CRC"))

    def setupFunctionality(self, MainWindow):
        self.disable_NA_functions()
        self.add_functions()
        self.add_options()
        self.center_app(MainWindow)

    def setupInitParams(self):
        self.h_running = False
        self.h_noise = 0
        self.h_chance = 0
        self.h_bits = 0
        self.h_shocks_remaining = 0

        self.c_running = False
        self.c_noise = 0
        self.c_chance = 0
        self.c_bits = 0
        self.c_shocks_remaining = 0

        self.crc_div_coeffs = []

        self.crc_div_polys = {"N/A": [], 
                            "CRC-8-CCITT": [1,0,0,0,0,0,1,1,1], 
                            "CRC-16-CCITT": [1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1]}
                            
        # "CRC-32": [1,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,1,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,1]
        # "CRC-64-ISO": [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        # 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1]

    def plot_graph(self, output_signal):
        tab = self.tabWidget.currentIndex()
        if tab == 0: 
            self.h_data_points = len(output_signal) * 10
            self.h_x = list(range(self.h_data_points))
            self.h_y = list(get_simple_graph(output_signal, datapoints=self.h_data_points))

            self.h_graph_mean = np.mean(self.h_y)
            self.h_y_noise = list(np.ones(self.h_data_points) * self.h_graph_mean)

            self.h_base_signal = self.h_y
            pen = pg.mkPen(color=(255, 120, 0))
            pen_noise = pg.mkPen(color=(255, 0, 0))
            self.h_data_line = self.h_graphWidget.plot(self.h_x, self.h_y, pen=pen)
            self.h_noise_line = self.h_graphWidget.plot(self.h_x, self.h_y_noise, pen=pen_noise)

            self.h_received_stream = []

            self.h_timer = QtCore.QTimer()
            self.change_timer()
            self.h_timer.timeout.connect(self.update_plot_data)
            self.h_timer.start()

        elif tab == 1: 
            self.c_data_points = len(output_signal) * 10
            self.c_x = list(range(self.c_data_points))
            self.c_y = list(get_simple_graph(output_signal, datapoints=self.c_data_points))

            self.c_graph_mean = np.mean(self.c_y)
            self.c_y_noise = list(np.ones(self.c_data_points) * self.c_graph_mean)

            self.c_base_signal = self.c_y
            pen = pg.mkPen(color=(255, 120, 0))
            pen_noise = pg.mkPen(color=(255, 0, 0))
            self.c_data_line = self.c_graphWidget.plot(self.c_x, self.c_y, pen=pen)
            self.c_noise_line = self.c_graphWidget.plot(self.c_x, self.c_y_noise, pen=pen_noise)
            
            self.c_received_stream = []

            self.c_timer = QtCore.QTimer()
            self.change_timer()
            self.c_timer.timeout.connect(self.update_plot_data)
            self.c_timer.start()

    def update_plot_data(self):
        tab = self.tabWidget.currentIndex()
        if tab == 0: 
            if self.h_running:
                self.h_x = self.h_x[1:]
                self.h_x.append(self.h_x[-1] + 1)

                self.h_y_noise = self.h_y_noise[1:]
                baseline = int(self.h_graph_mean * 100)
                noise = randint(baseline - self.h_noise,baseline + self.h_noise)
                self.h_y_noise.append(noise/100)
                
                if (self.h_shocks_remaining > 0):
                    if (randint(0,100) <= self.h_chance): 
                        noise *= 5
                        self.h_shocks_remaining -= 1

                self.h_base_signal = self.h_base_signal[1:] 
                self.h_base_signal.append(self.h_base_signal[0])
                
                self.h_y = self.h_y[1:]
                noise_effect = (noise - baseline)/100
                self.h_y.append(self.h_base_signal[0] + noise_effect)  

                self.h_data_line.setData(self.h_x, self.h_y)
                self.h_noise_line.setData(self.h_x, self.h_y_noise)

                self.receive_stream(self.h_base_signal[0] + noise_effect)
        elif tab == 1: 
            if self.c_running:
                self.c_x = self.c_x[1:]
                self.c_x.append(self.c_x[-1] + 1)

                self.c_y_noise = self.c_y_noise[1:]
                baseline = int(self.c_graph_mean * 100)
                noise = randint(baseline - self.c_noise,baseline + self.c_noise)
                self.c_y_noise.append(noise/100)

                if (self.c_shocks_remaining > 0):
                    if (randint(0,100) <= self.c_chance): 
                        noise *= 5
                        self.c_shocks_remaining -= 1

                self.c_base_signal = self.c_base_signal[1:] 
                self.c_base_signal.append(self.c_base_signal[0])
                
                self.c_y = self.c_y[1:]
                noise_effect = (noise - baseline)/100
                self.c_y.append(self.c_base_signal[0] + noise_effect)  

                self.c_data_line.setData(self.c_x, self.c_y)
                self.c_noise_line.setData(self.c_x, self.c_y_noise)

                self.receive_stream(self.c_base_signal[0] + noise_effect)

    def receive_stream(self, data):
        tab = self.tabWidget.currentIndex()
        if tab == 0: 
            self.h_received_stream.append(data)    
            if len(self.h_received_stream) >= (self.h_data_points-1):
                period = self.h_data_points / len(self.h_sent)
                bits_received = ''
                for i in range(len(self.h_sent)):
                    val = np.mean(self.h_received_stream[math.floor(i*period):math.floor((i+1)*period)])
                    if val <= self.h_graph_mean:
                        bits_received += '0'
                    else: bits_received += '1'
                self.update_log(self.h_sent, bits_received)

                self.h_received_stream = []
                self.h_shocks_remaining = self.h_bits * 10 #Because there's 10x bits datapoints
        elif tab == 1: 
            self.c_received_stream.append(data)    
            if len(self.c_received_stream) >= (self.c_data_points-1):
                period = self.c_data_points / len(self.c_sent)
                bits_received = ''
                for i in range(len(self.c_sent)):
                    val = np.mean(self.c_received_stream[math.floor(i*period):math.floor((i+1)*period)])
                    if val <= self.c_graph_mean:
                        bits_received += '0'
                    else: bits_received += '1'
                self.update_log(self.c_sent, bits_received)

                self.c_received_stream = []
                self.c_shocks_remaining = self.c_bits * 10 #Because there's 10x bits datapoints

    def update_log(self, sent, received):
        tab = self.tabWidget.currentIndex()
        now = datetime.now().time()
        
        if tab == 0: 
            deconstructed_message = []
            char_count = len(self.h_binary)
            for i in range(len(self.h_binary)):
                for idx, x in enumerate(received):
                    if (idx % char_count == i):
                        deconstructed_message.append(x)   
            output = ""
            data_sym = "0b"
            data, errors = hc.check_for_errors(deconstructed_message)
            for item in data:
                output += chr(int(data_sym + ''.join(str(e) for e in item), 2))    
            log_text = ("[{}] Sent: {}".format(now, self.h_input.toPlainText())) \
                + "\nBinary: {}".format(self.h_binary) \
                + "\nSent: {}".format(sent) \
                + "\nReveiced: {}".format(received) \
                + "\nErrors: {}".format(errors) \
                + "\nReconstructed message: {}".format(output)           
            self.h_received_log.setPlainText(log_text)

        elif tab == 1: 
            output = ""
            data, errors = crc.check_for_errors(received, self.crc_div_coeffs)
            for item in data:
                output += chr(int(''.join(str(e) for e in item), 2))    
            log_text = ("[{}] Sent: {}".format(now, self.c_input.toPlainText())) \
                + "\nBinary: {}".format(self.c_binary) \
                + "\nSent: {}".format(sent) \
                + "\nReveiced: {}".format(received) \
                + "\nErrors: {}".format(errors == 1) \
                + "\nReconstructed message: {}\n".format(output)        
            self.c_log.setPlainText(log_text)

    def center_app(self, window):
        frameGm = window.frameGeometry()
        screen = QtWidgets.QApplication.desktop().screenNumber(QtWidgets.QApplication.desktop().cursor().pos())
        centerPoint = QtWidgets.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        window.move(frameGm.topLeft())

    def add_options(self):
        self.h_sample_rate.addItems(["N/A","8000","16000","44100","48000","92000"])
        self.h_frequency.addItems(["N/A","8000","16000","44100","48000","92000"])
        self.c_crc_combo.addItems(list(self.crc_div_polys.keys()))

    def disable_NA_functions(self):
        #Lacking implementation
        self.h_frequency.setDisabled(True)
        self.h_sample_rate.setDisabled(True)
        self.h_signal_levels.setDisabled(True)

        #Temporary unavailable
        self.h_continue_button.setDisabled(True)
        self.h_pause_button.setDisabled(True)
        self.h_speed_slider.setDisabled(True)

        self.c_continue_button.setDisabled(True)
        self.c_pause_button.setDisabled(True)
        self.c_speed_slider.setDisabled(True)
        self.c_coeffs.setDisabled(True)

    def add_functions(self):
        self.c_exit_button.clicked.connect(QtCore.QCoreApplication.quit)
        self.c_pause_button.clicked.connect(self.stop_timer)
        self.c_continue_button.clicked.connect(self.start_timer)
        self.c_send_button.clicked.connect(self.send_data)
        self.c_speed_slider.valueChanged.connect(self.change_timer)
        self.c_noise_dial.valueChanged.connect(self.noise_change)
        self.c_shock_dial.valueChanged.connect(self.shock_change)
        self.c_chance_dial.valueChanged.connect(self.chance_change)

        self.h_exit_button.clicked.connect(QtCore.QCoreApplication.quit)
        self.h_pause_button.clicked.connect(self.stop_timer)
        self.h_continue_button.clicked.connect(self.start_timer)
        self.h_send_button.clicked.connect(self.send_data)
        self.h_speed_slider.valueChanged.connect(self.change_timer)
        self.h_noise_dial.valueChanged.connect(self.noise_change)
        self.h_shock_dial.valueChanged.connect(self.shock_change)
        self.h_chance_dial.valueChanged.connect(self.chance_change)

        self.c_custom_poly.clicked.connect(self.custom_poly_trigger)
        self.c_crc_combo.currentTextChanged.connect(self.change_poly)

    def change_poly(self, custom = False, coeffs = ''):
        if custom == True:
            self.crc_div_coeffs = []
            for i in coeffs:
                self.crc_div_coeffs.append(int(i))
            
        else: 
            self.crc_div_coeffs = self.crc_div_polys.get(self.c_crc_combo.currentText())
        coeff_string = ''.join(str(int(e)) for e in self.crc_div_coeffs)
        self.c_coeffs.setText(coeff_string)

    def custom_poly_trigger(self):
        if self.c_custom_poly.isChecked():
            self.c_coeffs.setEnabled(True)
            self.c_crc_combo.setEnabled(False)
            self.change_poly(True)
        else: 
            self.c_coeffs.setEnabled(False)
            self.c_crc_combo.setEnabled(True)
            self.change_poly(False)

    def start_timer(self):
        tab = self.tabWidget.currentIndex()

        if tab == 0: 
            self.h_continue_button.setEnabled(False)
            self.h_pause_button.setEnabled(True)
            self.h_speed_slider.setEnabled(True)
            self.h_timer.start()
        elif tab == 1: 
            self.c_continue_button.setEnabled(False)
            self.c_pause_button.setEnabled(True)
            self.c_speed_slider.setEnabled(True)
            self.c_timer.start()

    def stop_timer(self):
        tab = self.tabWidget.currentIndex()

        if tab == 0: 
            self.h_continue_button.setEnabled(True)
            self.h_pause_button.setEnabled(False)
            self.h_timer.stop()
        elif tab == 1: 
            self.c_continue_button.setEnabled(True)
            self.c_pause_button.setEnabled(False)
            self.c_timer.stop()

    def send_data(self):
        tab = self.tabWidget.currentIndex()
        if tab == 0: 
            if self.h_running == True: 
                self.h_data_line.clear()
                self.h_noise_line.clear()

            self.h_binary = hc.get_hamming_code(self.h_input.toPlainText())
            sent_stream = []
            block_size = len(self.h_binary[0])
            for i in range(block_size):
                for item in self.h_binary:
                    sent_stream.append(item[i])
            self.h_sent = ''.join([str(elem) for elem in sent_stream])
            self.plot_graph(self.h_sent)

            self.h_running = True
        elif tab == 1: 
            if self.c_custom_poly.isChecked():
                self.change_poly(True, self.c_coeffs.text())

            if self.c_running == True: 
                self.c_data_line.clear()
                self.c_noise_line.clear()
            
            div_poly = self.crc_div_coeffs
            self.c_binary = crc.get_CRC_code(self.c_input.toPlainText(), div_poly)

            self.c_sent = ''.join([str(elem) for elem in self.c_binary])
            self.plot_graph(self.c_sent)

            self.c_running = True

        self.start_timer()
        
    def noise_change(self):
        tab = self.tabWidget.currentIndex()
        if tab == 0: 
            self.h_noise = self.h_noise_dial.value()
            self.h_noise_label.setText('Noise level: {}'.format(self.h_noise))
        elif tab == 1: 
            self.c_noise = self.c_noise_dial.value()
            self.c_noise_label.setText('Noise level: {}'.format(self.c_noise))
    
    def chance_change(self):
        tab = self.tabWidget.currentIndex()
        if tab == 0: 
            self.h_chance = self.h_chance_dial.value()
            self.h_chance_label.setText('Shock chance: {}'.format(self.h_chance))
        elif tab == 1: 
            self.c_chance = self.c_chance_dial.value()
            self.c_chance_label.setText('Shock chance: {}'.format(self.c_chance))
    
    def shock_change(self):
        tab = self.tabWidget.currentIndex()
        if tab == 0: 
            self.h_bits = math.floor(self.h_shock_dial.value()/10)
            self.h_shocked_bits.setText('Shocked bits: {}'.format(self.h_bits))
        elif tab == 1: 
            self.c_bits = math.floor(self.c_shock_dial.value()/10)
            self.c_shocked_bits.setText('Shocked bits: {}'.format(self.c_bits))
        
    def change_timer(self):
        tab = self.tabWidget.currentIndex()
        if tab == 0: 
            speed = 100 - self.h_speed_slider.value()
            self.h_timer.setInterval(speed)
        elif tab == 1: 
            speed = 100 - self.c_speed_slider.value()
            self.c_timer.setInterval(speed)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.setupInitParams()
    ui.setupFunctionality(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())
