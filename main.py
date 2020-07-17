from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QLineEdit, QPushButton, QToolTip, QMessageBox, QVBoxLayout
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
import MySQLdb as mdb
import sys

class Window(QDialog):
    def __init__(self): #método construtor
        super().__init__()
        self.title = "Registration"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 550
        #self.iconName = "home.png"
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

        button1 = QPushButton('Submit', self)
        button1.move(340, 470)
        button1.resize(190, 40)
        button1.setStyleSheet('QPushButton {background-color: #C3EADD; font: normal; font-size: 20px}')
        #button1.clicked.connect(self.button1_click)

        self.InitWindow()

    def InitWindow(self):
        self.nuvem = QLabel(self)
        self.nuvem.setPixmap(QPixmap('nuvem2.png'))
        #self.nuvem.resize(400,200)
        
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setStyleSheet("QDialog {background: 'blach';}");

    #def button1_click(self):
     #   print('O botão submit foi clicado')

        self.show()
    def funcao_principal():#função que será acionada pelo botão
        linha1 = textBox.text()
        print('Name', linha1)
        linha2 = textBox_2.text()
        print('Birthdate', linha2)
        linha3 = textBox_3.text()
        print('Gender', linha3)
        linha4 = textBox_4.text()
        print('Email', linha4)
        linha5 = textBox_5.text()
        print('Phone', linha5)

        cursor = banco.cursor()#criamos um cursor e usamos nossa instancia do banco -> variavel criada fora da função principal
        comando_sql = 'insert into produtos(Name, Birthdate, Gender, Email, Phone) values(%s, %s, %s, %s, %s)'
        dados = (str(linha1), str(linha2), str(linha3), str(linha4), str(linha5))
        cursor.execute(comando_sql, dados)
        banco.commit()

        linha1 = textBox.setText("")
        linha2 = textBox_2.setText("")
        linha3 = textBox_3.setText("")
        linha4 = textBox_4.setText("")
        linha5 = textBox_5.setText("")

    app=QtWidgets.QApplication([])

    button1.clicked.connect(funcao_principal)
     
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())