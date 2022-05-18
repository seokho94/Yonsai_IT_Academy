import sys
from xml.dom.minidom import TypeInfo 
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets, uic
import finplot as fplt
from matplotlib.axis import YAxis
import pyupbit
import datetime
import time
import pandas as pd
from Current_price import total
from PyQt5.QtGui import *

##from Current_price import total

fplt.display_timezone = datetime.timezone.utc 
fplt.candle_bull_color = "#FF0000"
fplt.candle_bull_body_color = "#FF0000" 
fplt.candle_bear_color = "#0000FF"

ui = uic.loadUiType('coingui.Ui')[0]

class Worker(QThread, ui):
    timeout = pyqtSignal(pd.DataFrame)

    def __init__(self):
        super().__init__()

    def get_ohlcv(self):
        self.df = pyupbit.get_ohlcv(ticker="KRW-XRP", interval="minute1")
        self.df = self.df[['open', 'high', 'low', 'close']]
        self.df.columns = ['Open', 'High', 'Low', 'Close']

    def run(self):
        self.get_ohlcv()
        while True:
            data = pyupbit.get_current_price("KRW-XRP", verbose=True)
            price = data['trade_price']
            timestamp = data['trade_timestamp'] / 1000
            cur_min_timestamp = timestamp - timestamp % (60)
            cur_min_dt = datetime.datetime.fromtimestamp(cur_min_timestamp)

            if cur_min_dt > self.df.index[-1]:
                self.get_ohlcv()
            else:
                # update last candle
                self.df.iloc[-1]['Close'] = price
                if price > self.df.iloc[-1]['High']:
                    self.df.iloc[-1]['High'] = price
                if price < self.df.iloc[-1]['High']:
                    self.df.iloc[-1]['Low'] = price

            self.timeout.emit(self.df)
            time.sleep(1)


class MyWindow(QMainWindow, ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("CoinTrding")
        self.df = None
        self.plot = None

        # thread
        self.w = Worker()
        self.w.timeout.connect(self.update_data)
        self.w.start()

        # timer 
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.update)

        self.view = QGraphicsView()
        self.graph_verticalLayout.addWidget(self.view)
        ax0, ax1 = fplt.create_plot_widget(master=self.view, rows=2, init_zoom_periods=100)
        self.view.axs = [ax0, ax1]
        self.graph_verticalLayout.addWidget(ax0.ax_widget, 0, 0)
        self.graph_verticalLayout.addWidget(ax1.ax_widget, 1, 0)

        now = datetime.datetime.now()
        self.statusBar().showMessage(str(now))
        de = pyupbit.get_ohlcv(ticker="KRW-XRP", interval="minute1")
        fplt.candlestick_ochl(de[['open', 'close', 'high', 'low']], ax=ax0)
        fplt.volume_ocv(de[['open', 'close', 'volume']], ax=ax1)
        fplt.refresh()      # refresh autoscaling when all plots complete
        fplt.show(qt_exec=False)
        
        self.initUI()
        
        
    def update(self):
        now = datetime.datetime.now()
        self.statusBar().showMessage(str(now))

        if self.df is not None:
            if self.plot is None:
                self.plot = fplt.candlestick_ochl(self.df[['Open', 'Close', 'High', 'Low']])
                fplt.show(qt_exec=False)
            else:
                self.plot.update_data(self.df[['Open', 'Close', 'High', 'Low']])

    @pyqtSlot(pd.DataFrame)
    
    def update_data(self, df):
        self.df = df
          
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
                
        self.current_verlayout.addWidget(self.tableWidget)
        self.setLayout(self.current_verlayout)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()