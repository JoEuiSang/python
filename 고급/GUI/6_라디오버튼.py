import tkinter as tk


def f1():
    msg = '당신의 선택은' + str(val.get())
    label.config(text=msg)


root = tk.Tk()
root.geometry('300x300')
root.title('라디오버튼')
label = tk.Label(root, text='라디오테스트')
label.pack()

val = tk.IntVar()   #라디오 버튼을 그룹화할 변수

# variable로 그룹화, value로 값 구분
r1 = tk.Radiobutton(root, text='오렌지', variable=val, value=1, command=f1)
r1.pack()

r2 = tk.Radiobutton(root, text='사과', variable=val, value=2, command=f1)
r2.pack()

r3 = tk.Radiobutton(root, text='자몽', variable=val, value=3, command=f1)
r3.pack()

# 얘는 위에랑 별개 라디오버튼
val1 = tk.IntVar()
r4 = tk.Radiobutton(root, text='별개', variable=val1, value=3, command=f1)
r4.pack()

root.mainloop()
