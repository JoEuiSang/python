import tkinter as tk

def f1(e):
    print('왼')
    print(e.x, e.y)

def f2(e):
    print('오')
    print(e.x, e.y)

def f3(e):
    print('휠')
    print(e.x, e.y)


def f4(e):
    print('엔트리에 온마우스 이벤트 발생')

def f5(e):
    print('엔터키 누름')
    print(e.x, e.y)

root = tk.Tk()
b = tk.Button(root, text='btn',width = 30)
e = tk.Entry(root,width=30)
b.pack()
e.pack()

# 이벤트 핸들러를 등록하는 함수 bind
# bind로 핸들러를 등록하면 무조건 첫 파라미터로 이벤트 객체를 넘겨준다. self처럼

b.bind('<Button-1>',f1)  #<Button-1>: 왼쪽, 3: 가운데, 2: 오른쪽  (마우스 왼쪽버튼,오른쪽버튼,휠버튼)
b.bind('<Button-2>',f2)
b.bind('<Button-3>',f3)


e.bind('<Enter>',f4)
e.bind('<Return>', f5) #엔터키를 입력했을때 발생하는 이벤트
root.mainloop()