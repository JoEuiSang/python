import os
import threading
import socket
import tkinter as tk
from functools import partial

from PIL import ImageTk
from PIL import Image


class KioskClient:
    # class 변수 / static 변수 : 모든 객체가 공유
    ip = 'localhost'
    port = 9999

    def __init__(self):
        self.btnFrame = None
        self.conn_soc = None  # 서버와 연결된 소켓
        self.win = None
        self.menuFrame = None
        self.orderBtn = None
        self.exitBtn = None
        self.berger = None
        self.menuBtn = []
        self.menuName = []
        self.priceList = []
        self.sumPrice = 0
        self.imagePath = '../image/'

    def conn(self):
        self.conn_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn_soc.connect((KioskClient.ip, KioskClient.port))

    def setMenuFrame(self):
        self.menuFrame = tk.Frame(self.win)

        path = self.imagePath + '불고기버거.jpg'
        img = Image.open(path)  # 이미지 파일 오픈
        img = img.resize((100, 80))
        src = ImageTk.PhotoImage(image=img)  # 이미지 파일 tk에서 사용 가능하도록 변환
        self.berger = tk.Button(self.menuFrame, image=src, command=self.menuCilck)
        self.berger.grid(row=0, column=0)
        self.menuFrame.pack()

    def setBtnFrame(self):
        self.btnFrame = tk.Frame(self.win)
        self.orderBtn = tk.Button(self.btnFrame, text='주문하기', command=self.orderFinish())
        self.orderBtn.grid(row=0, column=0)
        self.btnFrame.pack()

    def menuCilck(self, menuName):
        print('menuName', menuName)
        temp = self.orderTemp2.cget('text')
        if temp == '':
            selectList = menuName
        else:
            selectList = temp + ',' + menuName

        self.orderTemp2.config(text=selectList)

    def setWindow(self):
        self.win = tk.Tk()
        self.win.title('주문 프로그램')
        self.win.geometry('400x500+100+100')

        # 메뉴프레임 시작
        self.menuFrame = tk.Frame(self.win)

        fileNameList = os.listdir(self.imagePath)
        print(fileNameList)
        srcList = []

        j = 0
        for idx, i in enumerate(fileNameList):
            print('i', i)
            name = i.split('.')  # jpg 떼어내기
            self.menuName.append(name[0])
            path = self.imagePath + i
            img = Image.open(path)  # 이미지 파일 오픈
            img = img.resize((100, 80))
            srcList.append(ImageTk.PhotoImage(image=img))
            self.menuBtn.append(
                tk.Button(self.menuFrame, text=i, image=srcList[idx],
                          command=partial(self.menuCilck, self.menuName[idx])))  # partial 이라는 대단한 것을 발견, 클로저와 연관

            # self.menuBtn[idx].bind('<Button-1>', lambda event: self.menuCilck(event, i['text']))
            if idx != 0 and idx % 3 == 0:
                j += 1
            print(j, ',', idx)
            self.menuBtn[idx].grid(row=j, column=idx % 3)

        self.menuFrame.pack()

        # 메뉴프레임 끝

        # 선택리스트 시작
        self.orderTemp1 = tk.Label(self.win, relief="sunken", text='이곳에 선택메뉴가 표시됩니다.', width=200, wraplength=200)
        self.orderTemp2 = tk.Label(self.win, relief="sunken", text='', width=200, wraplength=200)
        self.orderTemp1.pack()
        self.orderTemp2.pack()
        # 선택리스트 끝

        # 가격레이블시작
        self.priceLabel = tk.Label(self.win, text='')
        self.priceLabel.pack()
        # 가격레이블 끝

        # 버튼 프레임 시작
        self.btnFrame = tk.Frame(self.win)
        self.orderBtn = tk.Button(self.btnFrame, text='주문하기', command=self.orderFinish)
        self.orderBtn.grid(row=0, column=0)

        self.exitBtn = tk.Button(self.btnFrame, text='끝내기', command=self.exitSystem)
        self.exitBtn.grid(row=0, column=1)
        self.btnFrame.pack()

        # t1 = threading.Thread(target=self.setMenuFrame())
        # t2 = threading.Thread(target=self.setBtnFrame())
        #
        # t1.start()
        # t2.start()

        self.win.mainloop()

        #
        # self.orderBtn = tk.Button(self.win, width=10, text='주문')
        # self.orderBtn.bind('<Button-1>', self.orderFinish)
        # self.orderBtn.pack()

        # self.orderBtn.grid(row=1, column=1)

    def exitSystem(self):
        msg = '/exit'
        msg = msg.encode(encoding='utf-8')
        self.conn_soc.sendall(msg)
        print('종료신호전송')
        self.win.destroy()

    def orderFinish(self):  # 키보드 입력 받아 상대방에게 메시지 전송
        msg = self.orderTemp2.cget('text')
        self.orderTemp2.config(text='')
        msg = msg.encode(encoding='utf-8')
        self.conn_soc.sendall(msg)
        print('전송')

    def run(self):
        self.conn()
        self.setWindow()

    def close(self):
        self.conn_soc.close()
        print('종료되었습니다')


def main():
    conn = KioskClient()
    conn.run()


main()
