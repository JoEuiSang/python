import os
import socket, threading

import 고급.pos.svc.OrderSvc as oSvc
import 고급.pos.svc.EmpSvc as EmpSvc
import 고급.pos.svc.MenuSvc as MenuSvc
import tkinter as tk


class Room:  # 주문기 클래스.
    def __init__(self):
        self.clients = []
        self.allChat = None

    def addClient(self, c):  # c: 텔레마케터 . 클라이언트 1명씩 전담하는 쓰레드
        self.clients.append(c)

    def delClient(self, c):
        self.clients.remove(c)

    def sendMsgAll(self, msg):  # 채팅방에 있는 모든 사람한테 메시지 전송
        for i in self.clients:
            print(i)
            i.sendMsg(msg)


class Kiosks:  # 텔레마케터
    def __init__(self, r, soc, addr, kioskServer):
        self.room = r  # 채팅방. Room 객체
        self.addr = addr  # 키오스크 addr
        self.soc = soc  # 키오스크와 1:1 통신할 소켓
        self.svc = oSvc.OrderSvc()
        self.menuFrame = None
        self.server = kioskServer

    def addKioskFrame(self, server, addr):
        self.menuFrame = tk.Frame(server.win)
        addrLabel = tk.Label(self.menuFrame, relief="sunken", text='연결 : ' + str(addr))
        addrLabel.pack()
        self.menuFrame.pack()

    def delKioskFrame(self):
        self.menuFrame.destroy()

    def readOrder(self):
        while True:
            order = self.soc.recv(1024).decode()  # 키오스크가 전송한 주문표 읽음
            print(order)
            if order == '/exit':  # 종료 메시지이면 루프 종료
                print(self.addr, '과의 연결은 종료합니다')
                self.delKioskFrame()
                self.room.delClient(self)
                break
            else:
                print(self.addr, '에서 주문이 들어왔습니다:', order)
                self.server.history += str(self.addr) + ':' + order + '\n'
                self.server.historyLabel.config(text=self.server.history)
                self.svc.addOrder(order)

        print(self.addr, '과의 연결이 종료되었습니다')

    def sendMsg(self, msg):
        print(type(msg))
        self.soc.sendall(msg.encode(encoding='utf-8'))


class KioskServer:
    ip = 'localhost'  # or 본인 ip or 127.0.0.1
    port = 9999

    def __init__(self):
        self.server_soc = None  # 서버 소켓(대문)
        self.room = Room()
        self.clearBtn = None
        self.btnFrame = None
        self.mngBtnFrame = None
        self.win = None
        self.manageTk = None
        self.history = ''
        self.historyLabel = None

    def open(self):
        self.server_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_soc.bind((KioskServer.ip, KioskServer.port))
        self.server_soc.listen()

    def shutDown(self):
        self.win.destroy()

    def setManageMode(self):
        empsvc = EmpSvc.EmpSvc()
        menusvc = MenuSvc.MenuSvc()

        self.manageTk = tk.Toplevel(self.win)
        self.manageTk.title('관리모드')
        self.manageTk.geometry('400x500+100+100')

        self.BtnFrame = tk.Frame(self.manageTk)
        self.BtnFrame.pack()
        self.empBtn = tk.Button(self.BtnFrame, text='직원 관리', command=lambda: empsvc.empRun(self.manageTk))
        self.empBtn.grid(row=0, column=0)
        self.menuBtn = tk.Button(self.BtnFrame, text='메뉴 관리', command=lambda: menusvc.menuRun(self.manageTk))
        self.menuBtn.grid(row=0, column=1)
        exitBtn = tk.Button(self.BtnFrame, text='뒤로 가기', command=self.manageTk.destroy)
        exitBtn.grid(row=0, column=2)

    def manage(self):
        self.setManageMode()

    def setWindow(self):
        self.win = tk.Tk()
        self.win.title('관리 프로그램 (서버)')
        self.win.geometry('400x500+100+100')

        self.btnFrame = tk.Frame(self.win)
        self.btnFrame.pack()
        self.clearBtn = tk.Button(self.btnFrame, text='서버종료', command=self.shutDown)
        self.clearBtn.grid(row=0, column=0)
        self.mngBtn = tk.Button(self.btnFrame, text='관리모드', command=self.manage)
        self.mngBtn.grid(row=0, column=1)

        self.historyLabel = tk.Label(self.win, text='test')
        self.historyLabel.pack()

        self.win.mainloop()

    def run(self):
        self.open()
        print('서버 시작')
        thWin = threading.Thread(target=self.setWindow)
        thWin.start()

        while True:
            print('대기중')
            client_soc, addr = self.server_soc.accept()
            print(addr)
            print(addr, '접속')
            k = Kiosks(self.room, client_soc, addr, self)
            k.addKioskFrame(self, addr)
            self.room.addClient(k)
            print('클라:', self.room.clients)
            th = threading.Thread(target=k.readOrder)
            th.start()

        self.server_soc.close()


def main():
    cs = KioskServer()
    cs.run()


main()
