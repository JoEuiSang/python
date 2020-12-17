import tkinter as tk

root = tk.Tk()
root.title('타이틀')
root.geometry('300x200+100+100') #윈도우 창의 크기와 위치를 지정,(가로x세로+좌표(x,y))
root.resizable(False, False)    #크기 제어를 못하도록 막아둠


b1 = tk.Button(root, width=10, text = '1')
b1.grid(row=0, column=0)    # 표 형태로 배치 (행, 열)

b2 = tk.Button(root, width=10, text = '2')
b2.grid(row=0, column=1)

b3 = tk.Button(root, width=10, text = '3')
b3.grid(row=0, column=2)

b4 = tk.Button(root, width=10, text = '4')
b4.grid(row=1, column=0)

b5 = tk.Button(root, width=10, text = '5')
b5.grid(row=1, column=1)

b6 = tk.Button(root, width=5, text = '6')
b6.grid(row=1, column=2)

b7 = tk.Button(root, width=10, text = '7')
b7.place(x=100,y=100) # 위치를 좌표로 줄수있다


root.mainloop()