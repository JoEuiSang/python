import tkinter as tk
from functools import partial

import 고급.pos.dao.MenuDao as menuDao


class MenuSvc:
    def __init__(self):
        self.dao = menuDao.MenuDao()
        self.menuTk = None
        self.addTk = None
        self.upFrame = None
        self.menuInfo = None
        self.delBtns = []
        self.upBtns = []

    def menuRun(self, Tk):
        self.setWin(Tk)

    def setWin(self, Tk):
        self.menuTk = tk.Toplevel(Tk)
        self.menuTk.title('메뉴관리')
        self.menuTk.geometry('400x500+100+100')
        label = tk.Label(self.menuTk, text='쉽고 빠르게 메뉴관리를 시작하세요')
        label.pack()

        self.BtnFrame = tk.Frame(self.menuTk)
        self.BtnFrame.pack()
        self.showMenuBtn = tk.Button(self.BtnFrame, text='모든 메뉴 보기', command=self.showMenu)
        self.showMenuBtn.grid(row=0, column=0)
        self.addMenuBtn = tk.Button(self.BtnFrame, text='메뉴 추가', command=self.setAdd)
        self.addMenuBtn.grid(row=0, column=1)

        exit = tk.Button(self.BtnFrame, text='뒤로 가기', command=self.menuTk.destroy)
        exit.grid(row=0, column=2)

    def showMenu(self):
        self.upBtns.clear()
        self.delBtns.clear()

        print('고고고')
        result = self.dao.selectAll()

        print(len(result))
        if self.menuInfo is not None:
            self.menuInfo.destroy()

        self.menuInfo = tk.Frame(self.menuTk)

        id = tk.Label(self.menuInfo, relief="sunken", text='메뉴\n번호', width=5, pady=10)
        menuName = tk.Label(self.menuInfo, relief="sunken", text='메뉴명', width=10, pady=10)
        price = tk.Label(self.menuInfo, relief="sunken", text='가격', width=5, pady=10)
        kind = tk.Label(self.menuInfo, relief="sunken", text='종류', width=5, pady=10)
        stock = tk.Label(self.menuInfo, relief="sunken", text='재고', width=5, pady=10)
        id.grid(row=0, column=0)
        menuName.grid(row=0, column=1)
        price.grid(row=0, column=2)
        kind.grid(row=0, column=3)
        stock.grid(row=0, column=4)

        for idx, i in enumerate(result):
            id = tk.Label(self.menuInfo, relief="sunken", text=i.id, width=5, pady=10)
            menuName = tk.Label(self.menuInfo, relief="sunken", text=i.name, width=10, pady=10)
            price = tk.Label(self.menuInfo, relief="sunken", text=i.price, width=5, pady=10)
            kind = tk.Label(self.menuInfo, relief="sunken", text=i.kind, width=5, pady=10)
            stock = tk.Label(self.menuInfo, relief="sunken", text=i.stock, width=5, pady=10)

            id.grid(row=idx + 1, column=0)
            menuName.grid(row=idx + 1, column=1)
            price.grid(row=idx + 1, column=2)
            kind.grid(row=idx + 1, column=3)
            stock.grid(row=idx + 1, column=4)

            self.upBtns.append(tk.Button(self.menuInfo, text='수정', width=5, command=partial(self.upMenuFrame, i.id)))
            self.upBtns[idx].grid(row=idx + 1, column=5)
            self.delBtns.append(tk.Button(self.menuInfo, text='삭제', width=5, command=partial(self.delMenu, i.id, idx)))
            self.delBtns[idx].grid(row=idx + 1, column=6)
        self.menuInfo.pack()

    def setAdd(self):
        self.addTk = tk.Toplevel(self.menuTk)
        self.addTk.title('직원추가')
        self.addTk.geometry('400x500+100+100')
        label = tk.Label(self.addTk, text='어서오세요')
        label.pack()

        self.Frame = tk.Frame(self.addTk)
        self.Frame.pack()

        nameLabel = tk.Label(self.Frame, text='메뉴명 ')
        nameLabel.grid(row=0, column=0)
        self.nameEntry = tk.Entry(self.Frame)
        self.nameEntry.grid(row=0, column=1)

        priceLabel = tk.Label(self.Frame, text='가격 ')
        priceLabel.grid(row=1, column=0)
        self.priceEntry = tk.Entry(self.Frame)
        self.priceEntry.grid(row=1, column=1)

        kindLabel = tk.Label(self.Frame, text='종류')
        kindLabel.grid(row=2, column=0)
        self.kindEntry = tk.Entry(self.Frame)
        self.kindEntry.grid(row=2, column=1)

        self.addMenuBtn = tk.Button(self.Frame, text='추가하기', command=self.addMenu)
        self.addMenuBtn.grid(row=3, column=0)

        self.backBtn = tk.Button(self.Frame, text='취소하기')
        self.backBtn.bind('<Button-1>', lambda e: self.close(e, self.addTk))
        self.backBtn.grid(row=3, column=1)

    def close(self, e, frame):
        print(e.x)
        frame.destroy()

    def addMenu(self):
        name = self.nameEntry.get()
        price = self.priceEntry.get()
        kind = self.kindEntry.get()
        print('1:', name, price, kind)
        if name != '' and price != '' and kind != '' :
            self.dao.insertMenu(name, price, kind)
            print('뭔데')
            self.addTk.destroy()
        else:
            tk.messagebox.showinfo(title='오류', message='모두 입력하세요.')

    def upMenuFrame(self, id):
        self.upFrame = tk.Frame(self.menuTk)
        self.upFrame.pack()

        labelFrame = tk.Frame(self.upFrame)
        label = tk.Label(labelFrame, text=str(id) + '번을 수정합니다~~')
        label.pack()
        labelFrame.pack()

        editFrame = tk.Frame(self.upFrame)
        editFrame.pack()

        nameLabel = tk.Label(editFrame, text='메뉴명 ')
        nameLabel.grid(row=0, column=0)
        self.nameEntry = tk.Entry(editFrame)
        self.nameEntry.grid(row=0, column=1)

        priceLabel = tk.Label(editFrame, text='가격 ')
        priceLabel.grid(row=1, column=0)
        self.priceEntry = tk.Entry(editFrame)
        self.priceEntry.grid(row=1, column=1)

        kindLabel = tk.Label(editFrame, text='종류')
        kindLabel.grid(row=2, column=0)
        self.kindEntry = tk.Entry(editFrame)
        self.kindEntry.grid(row=2, column=1)

        stockLabel = tk.Label(editFrame, text='재고')
        stockLabel.grid(row=3, column=0)
        self.stockEntry = tk.Entry(editFrame)
        self.stockEntry.grid(row=3, column=1)

        self.addMenuBtn = tk.Button(editFrame, text='수정하기', command=lambda: self.upMenu(id))
        self.addMenuBtn.grid(row=4, column=0)

        self.backBtn = tk.Button(editFrame, text='취소하기', command=self.upFrame.destroy)
        self.backBtn.grid(row=4, column=1)

    def upMenu(self, id):
        name = self.nameEntry.get()
        price = self.priceEntry.get()
        kind = self.kindEntry.get()
        stock = self.stockEntry.get()

        self.dao.updateMenu(id, name, price, kind, stock)
        self.upFrame.destroy()
        self.showMenu()

    def delMenu(self, id):
        self.MenuInfo.destroy()
        self.dao.deleteMenu(id)

        self.showMenu()
