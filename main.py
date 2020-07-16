from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QMainWindow
import sys
from PyQt5.QtGui import QPixmap


class Window(QMainWindow):
    def __init__(self): #método construtor
        super().__init__()
        self.title = "PyQt5 Adding Image To Label"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 500
        self.iconName = "home.png"
        #self.setStyleSheet("background-color:black;"

        #self.label_1 = QLabel(self)
        #self.label_1.setText("Registration Info")
        #self.label_1.move(450,80)
        #self.label_1.setStyleSheet('QLabel {font: bold; font-size:20px; color: "black"}')
        #self.label_1.resize(150,25)

        self.InitWindow()

    def InitWindow(self):
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('nuvem2.png'))
        self.setGeometry(100000,50, 500,10000)
        
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setStyleSheet("QMainWindow {background: 'yellow';}");
        

        #vbox = QVBoxLayout()

       # labelImage = QLabel(self)
        #pixmap = QPixmap("nuvem2.png")
        #labelImage.setPixmap(pixmap)
        #self.setGeometry(60,50, 1000,400)
        #vbox.addWidget(labelImage)
        
        #label = QLabel("This Is PyQt5 Labels")
        #vbox.addWidget(label)
        #label2 = QLabel("This Is PyQt5 GUI Applicaition Development, Hello")
        #label2.setFont(QtGui.QFont("Sanserif", 20))
        #abel2.setStyleSheet('color:red')
        #vbox.addWidget(label2)

        
        #self.setLayout(vbox)
        self.show()
 
 
 
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())