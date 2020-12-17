import tkinter as tk

root = tk.Tk()
root.title('타이틀')
root.geometry('300x200+100+100') #윈도우 창의 크기와 위치를 지정,(가로x세로+좌표(x,y))
root.resizable(False, False)    #크기 제어를 못하도록 막아둠


b1 = tk.Button(root, width=10, text = 'left')
b1.pack(side ='left') #위치를 지정할수 있다.

b2 = tk.Button(root, width=10, text = 'right')
b2.pack(side ='right')

b3 = tk.Button(root, width=10, text = 'top')
b3.pack(side ='top')

b4 = tk.Button(root, width=10, text = 'bottom')
b4.pack(side ='bottom')


root.mainloop()