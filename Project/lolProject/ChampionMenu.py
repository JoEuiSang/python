import Project.lolProject.ChampionSvc as Svc

class Menu:
    def __init__(self):
        self.svc = Svc.Svc()
        self.itemSvc = None

    def run(self, itemsvc):
        print('챔피언 모드 시작!!')
        self.itemSvc = itemsvc
        while True:
            sel = int(input('1.챔피언 생성\t 2.챔피언 수정\t 3.챔피언 삭제\n'
                            '4.챔피언 검색\t 5.챔피언 전체 출력\t6.공격하기\n'
                            '7.아이템 구매\t 8.아이템 업그레이드\t 0.종료'))
            if sel == 1:
                self.svc.add_champion()
            elif sel == 2:
                self.svc.update_champion()
            elif sel == 3:
                self.svc.remove_champion()
            elif sel == 4:
                self.svc.select_champion()
            elif sel == 5:
                self.svc.select_all_champion()
            elif sel == 6:
                self.svc.fight_champion()
            elif sel == 7:
                if self.itemSvc is None:
                    print('아이템이 존재하지 않습니다\n아이템을 추가한 뒤 시도해주세요')
                    return
                self.svc.purchase_item(self.itemSvc)
            elif sel == 8:
                self.svc.mix_item()
            elif sel == 0:
                print('종료합니다')
                return
