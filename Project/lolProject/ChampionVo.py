class Champion:
    num = 0
    def __init__(self, data):
        Champion.num += 1
        self.num = Champion.num
        self.level = data['level']
        self.power = data['power']
        self.hp = data['hp']
        self.gold = data['gold']
        self.name = data['name']
        self.item = []  # 아이템을 여러개 가질수 잇으므로 리스트타입으로 선언

    def printInfo(self):
        keys = {'no': self.num,
                'name': self.name,
                'level': self.level,
                'power': self.power,
                'hp': self.hp,
                'gold': self.gold}
        if len(self.item) != 0:
            itemList = []
            for i in self.item:
                itemList.append(i['name'])
                itemList.append(i['grade'])
                itemList.append(i['power'])
                itemPack = itemList
            keys['item'] = itemPack

        for i in keys:
            if i == 'item' :
                for j in self.item:
                    print(f"아이템{j['num']} : {j['name']}, 등급 : {j['grade']}, 공격력 : {j['power']}")
            else:
                print(f'{i}\t : {keys[i]}')
        print('================================')