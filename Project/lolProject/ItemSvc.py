import Project.lolProject.ItemDao as itemDao
import Project.lolProject.ItemVo as itemVo


class Service:
    itemnum = 0

    def __init__(self):
        self.dao = itemDao.Dao()

    def searchItem(self):
        print('===================아이템 검색===================')
        if not self.dao.items:
            return print("등록된 아이템이 없습니다.")
        all = self.dao.selectall()
        for i in all:
            i.printProduct()
        num = int(input("검색할 아이템 번호: "))
        a = self.dao.search(num)
        if a != None:
            a.printProduct()
        else:
            print("없는 번호입니다.")

    def insertItem(self):
        print('===================아이템 생성===================')
        item = {}
        item['name'] = input("아이템 이름: ")
        item['price'] = int(input("아이템 가격: "))
        item['power'] = int(input("아이템 공격력: "))
        i = itemVo.Item(item)
        self.dao.insert(i)
        print(item['name'], '이 생성되었습니다\n')

    # 챔피언이 아이템 구매했을때
    def purchaseItem(self, itemNum):
        for (idx, i) in enumerate(self.dao.items):
            if i.num == itemNum:
                return i
        return None
        # print(cham.name)
        # item = {}
        # Service.itemnum += 1
        # item['num'] = Service.itemnum
        # item['name'] = input("아이템 이름: ")
        # item['price'] = int(input("아이템 가격: "))
        # item['power'] = int(input("아이템 공격력: "))
        # item['effect'] = input("아이템 효과: ")
        # item['grade'] = 'C'
        # return item

    def updateItem(self):
        print('===================아이템 수정===================')
        if not self.dao.items:
            return print("등록된 아이템이 없습니다.")
        self.selectAllItem()

        num = int(input("업데이트 할 아이템 번호: "))
        x = int(input("업데이트 할 정보: 1.아이템 가격  2.아이템 공격력  3.아이템 효과  "))
        while True:
            if x == 1:
                y = input("업데이트 할 아이템 가격: ")
                break
            elif x == 2:
                y = input("업데이트 할 아이템 공격력: ")
                break
            elif x == 3:
                y = input("업데이트 할 아이템 효과: ")
                break
            else:
                print("번호를 다시 입력하세요.")
        self.dao.update(num, x, y)

    def deleteItem(self):
        print('===================아이템 삭제===================')
        if not self.dao.items:
            return print("등록된 아이템이 없습니다.")
        num = int(input("삭제할 아이템 번호: "))
        self.dao.delete(num)

    def selectAllItem(self):
        print('===================아이템 목록===================')
        all = self.dao.selectall()
        if all is not None:
            for i in all:
                i.printProduct()
            return True
        else:
            print("등록된 아이템이 없습니다.")
            return None

    def mixItem(self):
        print('===================아이템 업그레이드===================')
        all = self.dao.selectall()
        if len(all) >= 2:
            for i in all:
                i.printProduct()
        else:
            print('아이템이 2개이상 필요합니다')
            return

        # if not self.dao.items:
        #     return print("등록된 아이템이 없습니다.")
        num1, num2 = map(int, input("조합할 아이템 번호 2개를 입력하세요(띄어쓰기로 입력): ").split())
        self.dao.mix(num1, num2)

    def mixItemCham(self, cham):
        # for i in cham.item:
        #     print(f"num: 1, 'name': 'q', 'price': 1, 'power': 1, 'grade': 'C'")
        itemNum1, itemNum2 = map(int, input("조합할 아이템 번호 2개를 입력하세요(띄어쓰기로 입력): ").split())
        self.dao.mix_item(itemNum1, itemNum2, cham)
