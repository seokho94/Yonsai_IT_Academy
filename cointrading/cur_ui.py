import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import current_ALL as cur
import time

# class Thread1(QThread):
#     #parent = MainWidget을 상속 받음.
#     def __init__(self, parent=QWidget):
#         super().__init__(parent)
#     def run(self):
#         myapp = MyApp
#         myapp.update(self)
#         time.sleep(1)

class MyApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        # self.update_data()

    def initUI(self):

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(114)
        self.tableWidget.setColumnCount(3)

        for row in range(114) :
            for col in range(3) :
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(cur.cur_data[row][col])))

        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)

        self.setWindowTitle('PyQt5 - QTableWidget')
        self.setGeometry(300, 100, 600, 400)
        self.show()
    
    # def update_data(self) :
    #     update = Thread1(self)
    #     update.start()
    
    # def update(self) :
    #     cur.current_all()
    #     for row in range(114) :
    #         for col in range(3) :
    #             update_item = self.tableWidget.item(row,col)
    #             print(update_item)
    
if __name__ == '__main__':
    cur.start()
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())