import Project.lolProject.ChampionDao as Dao_cham
import Project.lolProject.ItemSvc as itemSvc


class Svc:
    purItemNum=0
    def __init__(self):
        self.dao = Dao_cham.Dao_cham()
        # self.item_dao = item.Dao()
        self.item_svc = itemSvc.Service()

    def add_champion(self):
        print('=============================챔피언 생성=============================')
        keys = ['name', 'level', 'power', 'hp', 'gold']
        data = dict()
        for (idx, i) in enumerate(keys):
            if idx in range(1, len(keys)):
                # i == 'level' or i == 'power' or i == 'gold' or i == 'hp'
                data[i] = int(input(i + ' 입력 : '))
                continue
            data[i] = input(i + ' 입력 : ')
        self.dao.insert_champion(data)
        print(f'\n{data[keys[0]]}이 생성되었습니다\n')


    def select_all_champion(self):
        print('=============================챔피언 목록=============================')
        all = self.dao.selectAll_champion()
        if all is None:
            return None
        for i in all:
            i.printInfo()
        return True

    def update_champion(self):
        isdata = self.select_all_champion()
        if isdata == None:
            print('챔피언이 없습니다. 챔피언을 생성해주세요')
            return

        num = int(input('수정할 챔피언의 번호를 입력하세요'))
        # 있는 번호인지 체크
        champion = self.dao.check_num(num)
        if champion:
            # 있으면 수정내용 입력
            keys = ['level', 'power', 'gold', 'hp']
            data = dict()
            for i in keys:
                data[i] = int(input('수정할 ' + i + ' 입력 : '))
            self.dao.update_champion(champion, data)  # 번호와 수정데이터 넘김
            print('챔피언이 수정되었습니다')


    def remove_champion(self):
        print('=============================챔피언 삭제=============================')
        isdata = self.select_all_champion()
        if isdata == None:
            print('챔피언이 없습니다. 챔피언을 생성해주세요')
            return

        num = int(input('삭제할 챔피언의 번호를 입력하세요'))
        # 있는 번호인지 체크
        champion = self.dao.check_num(num)
        if champion:
            # 있으면 삭제
            self.dao.remove_champion(num)  # 번호 넘김
            print('챔피언이 삭제되었습니다')
        else:
            print('없는 번호입니다')

    def select_champion(self):
        print('=============================챔피언 검색=============================')
        isdata = self.select_all_champion()
        if isdata == None:
            print('챔피언이 없습니다. 챔피언을 생성해주세요')
            return

        num = int(input('검색할 챔피언의 번호를 입력하세요'))
        # 있는 번호인지 체크
        champion = self.dao.check_num(num)
        if champion:
            self.dao.select_champion(num)  # 번호와 수정데이터 넘김

    def fight_champion(self):
        print('=============================전투 모드=============================')
        isdata = self.select_all_champion()
        if isdata == None:
            print('챔피언이 없습니다. 챔피언을 생성해주세요')
            return

        attacker = int(input('공격을 가하는 챔피언 번호 입력'))
        attacker = self.dao.check_num(attacker)
        target = int(input('공격을 당하는 챔피언 번호 입력'))
        target = self.dao.check_num(target)
        self.dao.fight_champion(attacker, target)

    def purchase_item(self, itemSvc):
        print('=============================상 점=============================')
        self.select_all_champion()
        cham = int(input('아이템을 구매할 챔피언 번호 입력'))
        # 챔피언이 있으면, 챔피언정보 반환
        cham = self.dao.check_num(cham)
        if cham is None:
            print('그런 챔피언은 없습니다')
            return


        print('=========아이템 목록=========')
        success = itemSvc.selectAllItem()
        if success is None:
            print('아이템이 존재하지 않습니다\n아이템을 추가한 뒤 시도해주세요\n')
            return
        itemNum = int(input('구매를 원하는 아이템 번호 입력'))
        result = itemSvc.purchaseItem(itemNum)
        if result is None:
            print('그런 아이템은 없습니다')

        if cham.gold < result.price:
            print('돈이 모자랍니다')
            return

        item = {}
        item['chamNum'] = cham.num
        Svc.purItemNum += 1
        item['num'] = Svc.purItemNum
        item['name'] = result.name
        item['price'] = result.price
        item['power'] = result.power
        item['grade'] = result.grade

        self.dao.purchase_item(item,cham)

    def mix_item(self):
        print('=============================대 장 간=============================')
        cham = int(input('아이템을 조합할 챔피언 번호 입력'))
        self.select_all_champion()
        # 챔피언이있으면, 챔피언정보 반환
        cham = self.dao.check_num(cham)
        if len(cham.item) < 2:
            print('아이템이 한개밖에 없습니다.')
            return
        self.item_svc.mixItemCham(cham)
