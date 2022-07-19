from tkinter import *


class Calculator(Frame):
    global activeStr
    global stack
    def __init__(self):
        super(Calculator, self).__init__(window)
        self.build()


    def build(self):
        self.formula = "0"
        self.lbl = Label(text=self.formula, font=("Times New Roman", 21, "bold"), bg='#08E8DE', foreground="#FFF")
        self.lbl.place(x=11, y=40)

        btns = [
            "C", "DEL", "*", "=",
            "7", "8", "9", "/",
            "4", "5", "6", "+",
            "1", "2", "3", "-",
            "+/-", "0", "%", "."
        ]
        x = 10
        y = 90
        for bt in btns:
            com = lambda x=bt: self.logicalc(x)
            Button(text=bt, bg='#EB78F2', fg='white',
                   font=("Times New Roman", 15),
                   command=com).place(x=x, y=y,
                                      width=70, height=70)
            x += 70
            if x > 280:
                x = 10
                y += 70


    def logicalc(self, operation, x, y):
        if operation.isdigit:
            x += str(self.formula)
        if operation == 'C':
            self.formula = ''
        elif operation == 'DEL':
            self.formula = self.formula[0:-1]
        elif operation == '=':
            self.formula = x
        else:
            if self.formula == '0':
                self.formula = ''
            self.formula += operation
        self.update()


    def update(self):
        if self.formula == '':
            self.formula = '0'
        self.lbl.configure(text=self.formula)

if __name__ == '__main__':
    window = Tk()
    window.title('app')
    window['bg'] = '#08E8DE'
    window.geometry('300x450+200+200')
    app = Calculator()
    app.pack()
    window.mainloop()
