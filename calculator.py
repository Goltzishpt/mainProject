import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QIcon


digit = '0'


class Calculator(QWidget):
    def __init__(self):
        super(Calculator, self).__init__()
        self.initUI()


    def initUI(self):
        self.lbl = QLabel(digit, self)
        self.lbl.move(30, 50)

        self.btnC = QPushButton('C', self)
        self.btnC.setGeometry(15, 100, 80, 80)
        self.btnDel = QPushButton('del', self)
        self.btnDel.setGeometry(95, 100, 80, 80)
        self.btnStar = QPushButton('*', self)
        self.btnStar.setGeometry(175, 100, 80, 80)
        self.btnEqual = QPushButton('=', self)
        self.btnEqual.setGeometry(255, 100, 80, 80)

        self.btn7 = QPushButton('7', self)
        self.btn7.setGeometry(15, 180, 80, 80)
        self.btn8 = QPushButton('8', self)
        self.btn8.setGeometry(95, 180, 80, 80)
        self.btn9 = QPushButton('9', self)
        self.btn9.setGeometry(175, 180, 80, 80)
        self.btnDiv = QPushButton('/', self)
        self.btnDiv.setGeometry(255, 180, 80, 80)

        self.btn4 = QPushButton('4', self)
        self.btn4.setGeometry(15, 260, 80, 80)
        self.btn5 = QPushButton('5', self)
        self.btn5.setGeometry(95, 260, 80, 80)
        self.btn6 = QPushButton('6', self)
        self.btn6.setGeometry(175, 260, 80, 80)
        self.btnPlus = QPushButton('+', self)
        self.btnPlus.setGeometry(255, 260, 80, 80)

        self.btn1 = QPushButton('1', self)
        self.btn1.setGeometry(15, 340, 80, 80)
        self.btn2 = QPushButton('2', self)
        self.btn2.setGeometry(95, 340, 80, 80)
        self.btn3 = QPushButton('3', self)
        self.btn3.setGeometry(175, 340, 80, 80)
        self.btnMinus = QPushButton('-', self)
        self.btnMinus.setGeometry(255, 340, 80, 80)

        self.btn0 = QPushButton('0', self)
        self.btn0.setGeometry(15, 420, 160, 80)
        self.btnPercent = QPushButton('%', self)
        self.btnPercent.setGeometry(175, 420, 80, 80)
        self.btnDot = QPushButton('.', self)
        self.btnDot.setGeometry(255, 420, 80, 80)\

        self.setGeometry(300, 300, 350, 515)
        self.setWindowIcon(QIcon('imgCalc.png'))
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    c = Calculator()
    c.setWindowTitle('Calculator')  # заголовок
    sys.exit(app.exec_())  # вход в главный цикл


'''        self.btn3.clicked.connect(self.onClick3)
'''
