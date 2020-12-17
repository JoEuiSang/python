import tkinter as tk

def f1():
    #엔트리의 값을 반환
    s=entry.get()
    #라벨에 셋팅
    label.config(text=s)
    #엔트리의 모든 값 삭제
    entry.delete(0,tk.END)

root = tk.Tk()
root.title('제목입니다')
root.geometry('300x200+100+100')
root.resizable(False, False)
label = tk.Label(root, width=10, text = '라벨')
label.grid(row=0, column=0)

# 입력 박스
entry = tk.Entry(root, width=10)
entry.grid(row=1, column=0)

b1 = tk.Button(root, text='write', command = f1)
b1.grid(row=1, column=1)

root.mainloop()