from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import * 

import sys

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setFixedSize(600,600)
    
        self.setWindowTitle("Speed Learning Time Converter") #sets the window title

        
        placeholder = QLabel('')
        self.setCentralWidget(placeholder)
       
        
    

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()