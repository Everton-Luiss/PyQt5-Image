from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel
import sys
from PyQt5.QtGui import QPixmap


class Window(QDialog):
    def __init__(self): #método construtor
        super().__init__()
        self.title = "PyQt5 Adding Image To Label"
        self.top = 200
        self.left = 100
        self.width = 400
        self.height = 300
        self.iconName = "home.png"

        self.label_1 = QLabel(self)
        self.label_1.setText("Registration Info")
        self.label_1.move(450,80)
        self.label_1.setStyleSheet('QLabel {font: bold; font-size:20px}')
        self.label_1.resize(200,25)
        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        vbox = QVBoxLayout()

        labelImage = QLabel(self)
        pixmap = QPixmap("nuvem2.png")
        labelImage.setPixmap(pixmap)
        vbox.addWidget(labelImage)
        
        label = QLabel("This Is PyQt5 Labels")
        vbox.addWidget(label)
        label2 = QLabel("This Is PyQt5 GUI Applicaition Development, Hello")
        label2.setFont(QtGui.QFont("Sanserif", 20))
        label2.setStyleSheet('color:red')
        vbox.addWidget(label2)

        
        self.setLayout(vbox)
        self.show()
 
 
 
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())