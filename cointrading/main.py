import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
import Current_price

ui = uic.loadUi('coingui.Ui')[0]
class MainWindow(QWidget, ui):
  def __init__ (self):
    super().__init__()
    self.setupUi(self)
    self.setWindowTitle("CoinTrding")
  def show(self):
    data = [1,2,3,4]
    self.QTableWidget.setItem(1,1,QTableWidgetItem(str(data[0])))
    
"""
class QL(QGridLayout):
  def __init__(self):
    super().__init__()
    self.ui = uic.loadUi("coingui.ui",self)
    self.show()
  def show(self):
    data = [1,2,3,4]
    self.tableWidget_3.setItem(1,1,QTableWidgetItem(str(data[0])))
"""
  
if __name__ == "__main__":
  app = QtWidgets.QApplication(sys.argv)
  main_window = MainWindow()
  main_window.show()
  app.exec_()
