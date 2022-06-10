import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import current_ALL as cur
import time

class Thread1(QThread):
    #parent = MainWidget을 상속 받음.
    def __init__(self, parent=QWidget):
        super().__init__(parent)
        self.run()
        
    def run(self):
        myapp = MyApp
        myapp.update(self)
        time.sleep(1)

class MyApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        # self.update_data()

    def initUI(self):

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(114)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.resizeColumnToContents
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setHorizontalHeaderLabels(["코인명/심볼" ,"전일대비" , "현재가" ])
        
        for row in range(114) :
            for col in range(3) :
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(cur.cur_data[row][col])))
                
        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)

        self.setWindowTitle('PyQt5 - QTableWidget')
        self.setGeometry(300, 100, 600, 400)
        self.show()
    
    def update_data(self) :
        update = Thread1(self)
        update.start()
    
    def update(self) :
        self.tableWidget = QTableWidget()
        for row in range(114) :
            for col in range(1,3) :
                self.tableWidget.takeItem(row,col)
                self.tableWidget.setItem(row,col, str(cur.cur_data[row][col]))
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())