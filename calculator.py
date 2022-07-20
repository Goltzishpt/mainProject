import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon

class Calculator(QWidget):

    def __init__(self):
        super(Calculator, self).__init__()

        self.initUI()

    def initUI(self):
        btnC = QPushButton('C', self)
        btnC.setGeometry(15, 100, 80, 80)
        btnDel = QPushButton('del', self)
        btnDel.setGeometry(95, 100, 80, 80)
        btnStar = QPushButton('*', self)
        btnStar.setGeometry(175, 100, 80, 80)
        btnEqual = QPushButton('=', self)
        btnEqual.setGeometry(255, 100, 80, 80)

        btn7 = QPushButton('7', self)
        btn7.setGeometry(15, 180, 80, 80)
        btn8 = QPushButton('8', self)
        btn8.setGeometry(95, 180, 80, 80)
        btn9 = QPushButton('9', self)
        btn9.setGeometry(175, 180, 80, 80)
        btnDiv = QPushButton('/', self)
        btnDiv.setGeometry(255, 180, 80, 80)

        btn4 = QPushButton('4', self)
        btn4.setGeometry(15, 260, 80, 80)
        btn5 = QPushButton('5', self)
        btn5.setGeometry(95, 260, 80, 80)
        btn6 = QPushButton('6', self)
        btn6.setGeometry(175, 260, 80, 80)
        btnPlus = QPushButton('+', self)
        btnPlus.setGeometry(255, 260, 80, 80)

        btn1 = QPushButton('1', self)
        btn1.setGeometry(15, 340, 80, 80)
        btn2 = QPushButton('2', self)
        btn2.setGeometry(95, 340, 80, 80)
        btn3 = QPushButton('3', self)
        btn3.setGeometry(175, 340, 80, 80)
        btnMinus = QPushButton('-', self)
        btnMinus.setGeometry(255, 340, 80, 80)

        btn0 = QPushButton('0', self)
        btn0.setGeometry(15, 420, 160, 80)
        btnPercent = QPushButton('%', self)
        btnPercent.setGeometry(175, 420, 80, 80)
        btnDot = QPushButton('.', self)
        btnDot.setGeometry(255, 420, 80, 80)


        self.setGeometry(300, 300, 350, 515)
        self.setWindowIcon(QIcon('imgCalc.png'))
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    c = Calculator()
    c.setWindowTitle('Calculator')  # заголовок
    sys.exit(app.exec_())  # вход в главный цикл
