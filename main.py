from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QMainWindow, QLineEdit, QPushButton, QToolTip
import sys
from PyQt5.QtGui import QPixmap


class Window(QDialog):
    def __init__(self): #método construtor
        super().__init__()
        self.title = "PyQt5 Adding Image To Label"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 550
        self.iconName = "home.png"
        #self.setStyleSheet("background-color:black;"

        self.textBox = QLineEdit(self)
        self.textBox.move(430, 115)
        self.textBox.resize(250, 20)

        self.textBox_2 = QLineEdit(self)
        self.textBox_2.move(445, 182)
        self.textBox_2.resize(230, 20)

        self.textBox_3 = QLineEdit(self)
        self.textBox_3.move(445, 252)
        self.textBox_3.resize(230, 20)

        self.textBox_4 = QLineEdit(self)
        self.textBox_4.move(445, 325)
        self.textBox_4.resize(230, 20)

        self.textBox_5 = QLineEdit(self)
        self.textBox_5.move(445, 397)
        self.textBox_5.resize(230, 20)

        Button1 = QPushButton('Submit', self)
        Button1.move(340, 470)
        Button1.resize(190, 40)
        #Button1.setStyleSheet('QPushButton {background-collor: #0FB328; font: normal; font-size: 20px}')
        #Button1.clicked.connect(self.Button1_click)

        self.label_1 = QLabel(self)
        self.label_1.setText("Registration Info")
        self.label_1.move(430,50)
        self.label_1.setStyleSheet('QLabel {font: bold; font-size:20px; color: "white"}')
        self.label_1.resize(170,25)

        self.label_2 = QLabel(self)
        self.label_2.setText("Name")
        self.label_2.move(350,110)
        self.label_2.setStyleSheet('QLabel {font: normal; font-size:20px; color: "white"}')
        self.label_2.resize(170,25)

        self.label_3 = QLabel(self)
        self.label_3.setText("Birthdate")
        self.label_3.move(350,180)
        self.label_3.setStyleSheet('QLabel {font: normal; font-size:20px; color: "white"}')
        self.label_3.resize(170,25)

        self.label_4 = QLabel(self)
        self.label_4.setText("Gender")
        self.label_4.move(350,250)
        self.label_4.setStyleSheet('QLabel {font: normal; font-size:20px; color: "white"}')
        self.label_4.resize(170,25)

        self.label_5 = QLabel(self)
        self.label_5.setText("Email")
        self.label_5.move(350,320)
        self.label_5.setStyleSheet('QLabel {font: normal; font-size:20px; color: "white"}')
        self.label_5.resize(170,35)

        self.label_6 = QLabel(self)
        self.label_6.setText("Phone")
        self.label_6.move(350,400)
        self.label_6.setStyleSheet('QLabel {font: normal; font-size:20px; color: "white"}')
        self.label_6.resize(170,20)

        self.InitWindow()

    def InitWindow(self):
        self.nuvem = QLabel(self)
        self.nuvem.setPixmap(QPixmap('nuvem2.png'))
        #self.nuvem.resize(400,200)
        
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setStyleSheet("QDialog {background: 'blach';}");

    #def Button1_click(self):
     #   print('O botão submit foi clicado')

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