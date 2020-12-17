import tkinter as tk


def f1():
    if label.cget('text') == 'hello world' :  # .cget('text') : text 속성을 가져오기
        label.config(text='bye world')   #config(): 레이블 속성 변경 함수
    else :
        label.config(text='hello world')  # config(): 레이블 속성 변경 함수


window = tk.Tk()  # tk 객체 생성, 기본 윈도우 객체
label = tk.Label(window, text='hello wolrd')  # 뷰 위젯의 하나인 레이블객체 생성 (hello world 출력)
label.pack()  # pack을 이용해서 위젯(레이블,버튼 등...)을  윈도우 창에 배치를 함

btn = tk.Button(window, text='btn1', command=f1, width='50', height='10')
btn.pack()

window.mainloop()  # ui 쓰레드 실행하여 화면에 출력
