class Dao:
    def __init__(self):
        self.items = []

    def search(self, num):
        for idx, i in enumerate(self.items):
            if i.num == num:
                return self.items[idx]
        return None

    def insert(self, i):
        self.items.append(i)

    def update(self, num, x, y):
        arr = ['가격', '공격력', '효과']
        for idx, i in enumerate(self.items):
            if i.num == num:
                if x == 1:
                    i.price = y
                elif x == 2:
                    i.power = y
                else:
                    i.effect = y
                print(arr[x-1], "업데이트 완료")
                return
        print("없는 번호입니다.")

    def delete(self, num):
        for idx, i in enumerate(self.items):
            if i.num == num:
                print(f"{i.name} 삭제완료!")
                del self.items[idx]
                return
        return print("없는 아이템 번호입니다.")

    def selectall(self):
        if self.items is not None:
            return self.items
        else:
            return None

    def mix(self, num1, num2):
        for idx, i in enumerate(self.items):
            if i.num == num1:
                a, idx1 = i.grade, idx
        for idx, i in enumerate(self.items):
            if i.num == num2:
                b, idx2 = i.grade, idx
        if a == b:
            if a == 'A':
                print("이미 최상등급입니다.")
                return
            a = chr(ord(a) - 1)
            self.items[idx1].grade = a  # 등급적용
            # 이름,공격력 합치기
            self.items[idx1].name += self.items[idx2].name
            # 원래 무기 공격력 빼주기
            self.items[idx1].power = (self.items[idx1].power + self.items[idx2].power)*1.2
            # 업그레이드된 무기 공격력 1.2배
            # 뒤에 아이템 삭제
            print(f"{a}등급으로 조합완료")
            del self.items[idx2]

        else:
            print("아이템의 등급이 맞지 않습니다.")

    def mix_item(self, itemNum1, itemNum2, cham):
        a = ''
        b = ''
        # cham : 아이템을 조합할 챔피언 객체
        for idx, i in enumerate(cham.item):
            if i['num'] == itemNum1:
                a, idx1 = i['grade'], idx
        for idx, i in enumerate(cham.item):
            if i['num'] == itemNum2:
                b, idx2 = i['grade'], idx
                # chr(ord(a) - 1)
        if a == b:
            if a == 'A':
                print("이미 최상등급입니다.")
                return
            a = chr(ord(a) - 1)  # 등급올리기
            cham.item[idx1]['grade'] = a  # 등급적용
            # 이름 합치기
            cham.item[idx1]['name'] += cham.item[idx2]['name']
            #원래 무기 공격력 빼주기
            cham.power -= cham.item[idx1]['power'] + cham.item[idx2]['power']
            #업그레이드된 무기 공격력 1.2배
            cham.item[idx1]['power'] = (cham.item[idx1]['power'] + cham.item[idx2]['power']) * 1.2
            #업그레이드된 무기공격력 챔피언에 적용
            cham.power += cham.item[idx1]['power']
            # 뒤에 아이템 삭제
            del cham.item[idx2]
            print(f"{a}등급으로 조합완료")
        else:
            print("아이템의 등급이 맞지 않습니다.")
