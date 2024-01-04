import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QFileDialog
import matplotlib.pyplot as plt
import pandas as pd

class SalaryAnalyzer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Salary Analyzer")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.label = QLabel("Выберите файл с данными о зарплате:")
        self.layout.addWidget(self.label)

        self.button = QPushButton("Открыть файл", self)
        self.button.clicked.connect(self.load_data)
        self.layout.addWidget(self.button)

        self.central_widget.setLayout(self.layout)

        self.data = None
