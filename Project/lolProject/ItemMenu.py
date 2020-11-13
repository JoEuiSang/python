import Project.lolProject.ItemSvc as Svc

class Menu:
    def __init__(self):
        self.svc = Svc.Service()  #0000000001

    def run(self):
        print("아이템 모드 시작!!")
        while True:
            x = int(input('1.추가\t2.수정\t3.삭제\n4.검색\t5.전체출력\t6.조합\n0.종료\n'))
            if x == 1:
                self.svc.insertItem()
            elif x == 2:
                self.svc.updateItem()
            elif x == 3:
                self.svc.deleteItem()
            elif x == 4:
                self.svc.searchItem()
            elif x == 5:
                self.svc.selectAllItem()
            elif x == 6:
                self.svc.mixItem()
            elif x == 0:
                print("아이템 설정 종료 !")
                return self.svc
            else:
                print("번호를 다시 입력하세요.")