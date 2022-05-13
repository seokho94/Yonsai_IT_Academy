import sys
import py
import pyupbit as upbit
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
##from Current_price import total, output_data


ui = uic.loadUiType('coingui.Ui')[0]
class MainWindow(QMainWindow, ui):
  def __init__ (self):
    super().__init__()
    self.setupUi(self)
    self.setWindowTitle("CoinTrding")
    self.initUI()

  
if __name__ == "__main__":
  app = QApplication(sys.argv)
  main_window = MainWindow()
  main_window.show()
  app.exec_()