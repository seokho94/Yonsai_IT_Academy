import sys
from PyQt5.QtWidgets import *
from Current_price import total

class MyApp(QWidget) :
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        data = total()
        
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(11)
        self.tableWidget.setColumnCount(4)
        
        for i in range(11):
            for j in range(4):
                item = data[i][j]
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