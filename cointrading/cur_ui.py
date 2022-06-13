import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import current_ALL as cur
import time

class MyApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(114)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.resizeColumnToContents
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setHorizontalHeaderLabels(["코인명/심볼" ,"전일대비" , "현재가" ])
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        
        for row in range(114) :
            for col in range(3) :
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(cur.cur_data[row][col])))
                

        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)

        self.setWindowTitle('PyQt5 - QTableWidget')
        self.setGeometry(300, 100, 600, 400)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())