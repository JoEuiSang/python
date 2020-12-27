import tkinter as tk


def f1():
    msg = str(val1.get()) + ':' + str(val2.get()) +':'+str(val2.get())
    label.config(text=msg)


root = tk.Tk()
root.geometry('300x300')
root.title('체크박스')
label = tk.Label(root, text='체크박스 테스트')
label.pack()

val1 = tk.IntVar()   #라디오 버튼을 그룹화할 변수
val2 = tk.IntVar()   #라디오 버튼을 그룹화할 변수
val3 = tk.IntVar()   #라디오 버튼을 그룹화할 변수

# variable로 그룹화, value로 값 구분
c1 = tk.Checkbutton(root, text='오렌지', variable=val1)
c1.pack()

c2 = tk.Checkbutton(root, text='사과', variable=val2)
c2.pack()

c3 = tk.Checkbutton(root, text='자몽', variable=val3)
c3.pack()

b1 = tk.Button(root, text = '완료', command = f1)
b1.pack()

root.mainloop()
