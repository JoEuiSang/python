import tkinter as tk
import 고급.pos.dao.EmpDao as empDao
from tkinter import messagebox
from functools import partial


class EmpSvc:
    def __init__(self):
        self.dao = empDao.EmpDao()
        self.empTk = None
        self.addTk = None
        self.upFrame = None
        self.empInfo = None
        self.nameEntry = None
        self.pwEntry = None
        self.posiEntry = None
        self.delBtns = []
        self.upBtns = []
        self.delFlag = False
        self.upFlag = False

    def setAdd(self):
        self.addTk = tk.Toplevel(self.empTk)
        self.addTk.title('직원추가')
        self.addTk.geometry('400x500+100+100')
        label = tk.Label(self.addTk, text='어서오세요')
        label.pack()

        self.Frame = tk.Frame(self.addTk)
        self.Frame.pack()

        nameLabel = tk.Label(self.Frame, text='이름 ')
        nameLabel.grid(row=0, column=0)
        self.nameEntry = tk.Entry(self.Frame)
        self.nameEntry.grid(row=0, column=1)

        pwLabel = tk.Label(self.Frame, text='비밀번호 ')
        pwLabel.grid(row=1, column=0)
        self.pwEntry = tk.Entry(self.Frame)
        self.pwEntry.grid(row=1, column=1)

        posiLabel = tk.Label(self.Frame, text='직책코드')
        posiLabel.grid(row=2, column=0)
        self.posiEntry = tk.Entry(self.Frame)
        self.posiEntry.grid(row=2, column=1)

        self.addEmpBtn = tk.Button(self.Frame, text='추가하기', command=self.addEmp)
        self.addEmpBtn.grid(row=3, column=0)

        self.backBtn = tk.Button(self.Frame, text='취소하기')
        self.backBtn.bind('<Button-1>', lambda e: self.close(e, self.addTk))
        self.backBtn.grid(row=3, column=1)

    def close(self, e, frame):
        print(e.x)
        frame.destroy()

    def setWin(self, Tk):
        self.empTk = tk.Toplevel(Tk)
        self.empTk.title('직원관리')
        self.empTk.geometry('400x500+100+100')
        label = tk.Label(self.empTk, text='쉽고 빠르게 직원관리를 시작하세요')
        label.pack()

        self.BtnFrame = tk.Frame(self.empTk)
        self.BtnFrame.pack()
        self.showEmpBtn = tk.Button(self.BtnFrame, text='전체 직원 보기', command=self.showEmp)
        self.showEmpBtn.grid(row=0, column=0)
        self.addEmpBtn = tk.Button(self.BtnFrame, text='직원 추가', command=self.setAdd)
        self.addEmpBtn.grid(row=0, column=1)

        exit = tk.Button(self.BtnFrame, text='뒤로 가기', command=self.empTk.destroy)
        exit.grid(row=0, column=2)

    def addEmp(self):
        name = self.nameEntry.get()
        pw = self.pwEntry.get()
        pCode = self.posiEntry.get()
        print('1:', name, pw, pCode)
        if name != '' and pw != '' and pCode != '':
            self.dao.insertEmp(name, pw, pCode)
            print('뭔데')
            self.addTk.destroy()
        else:
            tk.messagebox.showinfo(title='오류', message='모두 입력하세요.')

    def showEmp(self):
        self.upBtns.clear()
        self.delBtns.clear()

        print('고고고')
        result = self.dao.selectAll()

        print(len(result))
        if self.empInfo is not None:
            self.empInfo.destroy()

        self.empInfo = tk.Frame(self.empTk)

        id = tk.Label(self.empInfo, relief="sunken", text='직원번호', width=10, pady=10)
        positionName = tk.Label(self.empInfo, relief="sunken", text='직책', width=10, pady=10)
        name = tk.Label(self.empInfo, relief="sunken", text='이름', width=10, pady=10)
        id.grid(row=0, column=0)
        positionName.grid(row=0, column=1)
        name.grid(row=0, column=2)

        for idx, i in enumerate(result):
            id = tk.Label(self.empInfo, relief="sunken", text=i.id, width=10)
            positionName = tk.Label(self.empInfo, relief="sunken", text=i.positionName, width=10)
            name = tk.Label(self.empInfo, relief="sunken", text=i.name, width=10)
            id.grid(row=idx + 1, column=0)
            positionName.grid(row=idx + 1, column=1)
            name.grid(row=idx + 1, column=2)

            # print('i.id', i.id, ', idx:', idx)
            # for u in self.upBtns:
            #     print('up:', u,',',u['text'])
            self.upBtns.append(tk.Button(self.empInfo, text='수정', width=5, command=partial(self.upEmpFrame, i.id)))
            self.upBtns[idx].grid(row=idx + 1, column=3)
            # for d in self.delBtns:
            #     print('del:', d,',',d['text'])
            self.delBtns.append(tk.Button(self.empInfo, text='삭제', width=5, command=partial(self.delEmp, i.id)))
            self.delBtns[idx].grid(row=idx + 1, column=4)
        self.empInfo.pack()

    def empRun(self, Tk):
        self.setWin(Tk)

    def delEmp(self, id):
        self.empInfo.destroy()
        self.dao.deleteEmp(id)

        self.showEmp()

    def upEmpFrame(self, id):
        self.upFrame = tk.Frame(self.empTk)
        self.upFrame.pack()

        labelFrame = tk.Frame(self.upFrame)
        label = tk.Label(labelFrame, text=str(id)+'번을 수정합니다~~')
        label.pack()
        labelFrame.pack()

        editFrame = tk.Frame(self.upFrame)
        editFrame.pack()

        nameLabel = tk.Label(editFrame, text='이름 ')
        nameLabel.grid(row=0, column=0)
        self.nameEntry = tk.Entry(editFrame)
        self.nameEntry.grid(row=0, column=1)

        pwLabel = tk.Label(editFrame, text='비밀번호 ')
        pwLabel.grid(row=1, column=0)
        self.pwEntry = tk.Entry(editFrame)
        self.pwEntry.grid(row=1, column=1)

        posiLabel = tk.Label(editFrame, text='직책코드')
        posiLabel.grid(row=2, column=0)
        self.posiEntry = tk.Entry(editFrame)
        self.posiEntry.grid(row=2, column=1)

        self.addEmpBtn = tk.Button(editFrame, text='수정하기', command=lambda :self.upEmp(id))
        self.addEmpBtn.grid(row=3, column=0)

        self.backBtn = tk.Button(editFrame, text='취소하기', command=self.upFrame.destroy)
        self.backBtn.grid(row=3, column=1)

    def upEmp(self, id):
        name = self.nameEntry.get()
        pw = self.pwEntry.get()
        pCode = self.posiEntry.get()

        print(name,pw,pCode)
        self.dao.updateEmp(id, name, pw, pCode)
        self.upFrame.destroy()
        self.showEmp()
