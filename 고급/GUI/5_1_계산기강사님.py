import tkinter as tk
import tkinter.font as tkFont


class Calculator:
    def __init__(self):
        self.root = None
        self.label = None

    def run(self):
        self.setWindow()

    def setWindow(self):
        self.root = tk.Tk()
        self.root.title('계산기')
        self.root.geometry('400x500+100+100')
        self.root.resizable(False, False)
        self.label = tk.Label(self.root, width=100, )
        self.label.grid(row=0, column=0)
        op = ['+', '-', '*', '/', 'C', '=']
        cnt = 0
        for i in range(0, 4):
            for j in range(0, 4):
                if 0 <= i <= 2:
                    txt = str(3 * i + 1)
                elif i == 2 and j == 0:
                    txt = '0'
                else:
                    txt = op[cnt]
                    cnt += 1
                b = tk.Button(self.root, text=txt)
                b.grid(row=i, column=j)

        self.label.config(text='s')

        self.root.mainloop()

    def btnClick(self, input):
        s = self.label.cget('text') + input
        print("dd", s)
        self.label.config(text=s)


def main():
    c = Calculator()
    c.run()


main()
