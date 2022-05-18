import sys
from PyQt5.QtWidgets import *
from Current_price import total
from PyQt5.QtGui import *


class MyApp(QWidget) :
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        ##global hlabel
        data = total()
        hlabel = data[0]
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(4)
        hlabel = data[0]
        self.tableWidget.setHorizontalHeaderLabels(hlabel)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        ##self.tableWidget.setVerticalHeader()
        
        for i in range(10):
            for j in range(4):
                item = data[i+1][j]
                self.tableWidget.setItem(i, j, QTableWidgetItem(item))
                
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