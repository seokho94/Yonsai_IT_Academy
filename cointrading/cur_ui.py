import sys
from PyQt5.QtWidgets import *
# import current_ALL as cur

class MyApp(QWidget):

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())