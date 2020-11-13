import Project.lolProject.ChampionVo as ChamVo


class Dao_cham:
    def __init__(self):
        self.champions = []

    def check_cham(self):
        if not self.champions:
            print("등록된 챔피언이 없습니다.")
            return True

    def insert_champion(self, data):
        self.champions.append(ChamVo.Champion(data))

    def selectAll_champion(self):
        if len(self.champions)!=0:
            return self.champions
        else: return None

    def update_champion(self, champion, data):
        # print(data)
        # for i in data:
        #     print(i,':',data[i])
        ##     champion.i = data[i] # 이 방법이 안되는데 어떻게하는 방법이 없나?
        champion.level = data['level']
        champion.power = data['power']
        champion.gold = data['gold']
        champion.hp = data['hp']

    def check_num(self, num):
        for i in self.champions:
            if i.num == num: return i
        return None

    def remove_champion(self, num):
        for (idx, i) in enumerate(self.champions):
            if i.num == num:
                del self.champions[idx]

    def select_champion(self, num):
        for (idx, i) in enumerate(self.champions):
            if i.num == num:
                i.printInfo()

    def get_index(self, num):
        for (idx, i) in enumerate(self.champions):
            if i.num == num:
                return idx

    def fight_champion(self, attacker, target):
        target.hp -= attacker.power
        if target.hp < 1:
            attacker.gold += target.gold
            attacker.level += 1
            attacker.power += 10
            print(target.name, '이 죽었습니다',
                  attacker.name, '\n골드+', target.gold,
                  '\n레벨 + 1\n공격력 + 10')
            self.remove_champion(target.num)
        else:
            print('공격에 성공하여', target.name, '의 체력이',
                  target.hp, '이 되었습니다')
        # self.champions[self.get_index(target)].hp -= \
        #     self.champions[self.get_index(attacker)].power
        # print('공격에 성공하여', self.champions[self.get_index(target)].name, '의 체력이',
        #       self.champions[self.get_index(target)].hp, '이 되었습니다')

    def add_item(self, item, cham):
        print(item['chamNum'], item['name'])
        cham.gold -= item['price']
        cham.power += item['power']
        idx = self.get_index(item['chamNum'])
        self.champions[idx].item.append(item)

    def purchase_item(self, item, cham):
        cham.item.append(item)
        cham.gold -= item['price']
        cham.power += item['power']
