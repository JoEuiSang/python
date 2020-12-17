import tkinter as tk


class Calc:
    def __init__(self, root):
        self.num1 = None
        self.num2 = None
        self.op = None
        self.result = None
        self.root = root
        self.uiInit()

    def uiInit(self):
        self.root.title('계산기')
        self.label = tk.Label(self.root, width=25)
        self.label.grid(row=0, column=0, columnspan=4)
        self.b1 = tk.Button(self.root, text='1', width=25, command=lambda: self.numBtn('1'))
        self.b1.grid(row=1, column=0)
        self.b2 = tk.Button(self.root, text='2', width=25, command=lambda: self.numBtn('2'))
        self.b2.grid(row=1, column=1)
        self.b3 = tk.Button(self.root, text='3', width=25, command=lambda: self.numBtn('3'))
        self.b3.grid(row=1, column=2)
        self.b4 = tk.Button(self.root, text='+', width=25, command=lambda: self.opBtn('+'))
        self.b4.grid(row=1, column=3)
        self.b5 = tk.Button(self.root, text='4', width=25, command=lambda: self.numBtn('4'))
        self.b5.grid(row=2, column=0)
        self.b6 = tk.Button(self.root, text='5', width=25, command=lambda: self.numBtn('5'))
        self.b6.grid(row=2, column=1)
        self.b7 = tk.Button(self.root, text='6', width=25, command=lambda: self.numBtn('6'))
        self.b7.grid(row=2, column=2)
        self.b8 = tk.Button(self.root, text='-', width=25, command=lambda: self.opBtn('-'))
        self.b8.grid(row=2, column=3)
        self.b9 = tk.Button(self.root, text='7', width=25, command=lambda: self.numBtn('7'))
        self.b9.grid(row=3, column=0)
        self.b10 = tk.Button(self.root, text='8', width=25, command=lambda: self.numBtn('8'))
        self.b10.grid(row=3, column=1)
        self.b11 = tk.Button(self.root, text='9', width=25, command=lambda: self.numBtn('9'))
        self.b11.grid(row=3, column=2)
        self.b12 = tk.Button(self.root, text='*', width=25, command=lambda: self.opBtn('*'))
        self.b12.grid(row=3, column=3)
        self.b13 = tk.Button(self.root, text='0', width=25, command=lambda: self.numBtn('0'))
        self.b13.grid(row=4, column=0)
        self.b14 = tk.Button(self.root, text='C', width=25, command=lambda: self.clear())
        self.b14.grid(row=4, column=1)
        self.b15 = tk.Button(self.root, text='=', width=25, command=lambda: self.resultBtn())
        self.b15.grid(row=4, column=2)
        self.b16 = tk.Button(self.root, text='/', width=25, command=lambda: self.opBtn('/'))
        self.b16.grid(row=4, column=3)

    def clear(self):
        self.num1 = None
        self.num2 = None
        self.op = None
        self.label.config(text='')

    def numBtn(self, num):
        txt = self.label.cget('text')
        txt += num
        if self.op is None:
            self.num1 = txt
            self.label.config(text=self.num1)
        else:
            self.num2 = txt
            self.label.config(text=self.num2)

    def opBtn(self, op):
        self.op = op
        self.label.config(text='')

    def resultBtn(self):
        if self.num1 is not None and self.num2 is not None:
            if self.op == '+':
                self.num1 = int(self.num1) + int(self.num2)
                self.num2= None
                self.label.config(text=self.num1)
            elif self.op == '-':
                self.num1 = int(self.num1) - int(self.num2)
                self.num2 = None
                self.label.config(text=self.num1)
            elif self.op == '*':
                self.num1 = int(self.num1) * int(self.num2)
                self.num2 = None
                self.label.config(text=self.num1)
            elif self.op == '/':
                self.num1 = int(self.num1) / int(self.num2)
                self.num2 = None
                self.label.config(text=self.num1)


def main():
    root = tk.Tk()
    c = Calc(root)
    root.mainloop()


main()
