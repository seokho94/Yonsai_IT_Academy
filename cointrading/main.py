import sys
import py
import pyupbit as upbit
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from Current_price import total


ui = uic.loadUiType('coingui.Ui')[0]
class MainWindow(QMainWindow, ui):
  def __init__ (self):
    super().__init__()
    self.setupUi(self)
    self.setWindowTitle("CoinTrding")
class QV(QGridLayout):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(2)
        self.tableWidget.setColumnCount(2)

        self.tableWidget.setItem(0, 0, QTableWidgetItem('Apple'))
        self.tableWidget.setItem(0, 1, QTableWidgetItem('Banana'))
        self.tableWidget.setItem(1, 0, QTableWidgetItem('Orange'))
        self.tableWidget.setItem(1, 1, QTableWidgetItem('Grape'))

        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)

        self.setWindowTitle('PyQt5 - QTableWidget')
        self.setGeometry(300, 100, 600, 400)
        self.show()

  
if __name__ == "__main__":
  app = QtWidgets.QApplication(sys.argv)
  main_window = MainWindow()
  main_window.show()
  app.exec_()
