class Item:
    num = 0
    def __init__(self, item):
        Item.num += 1
        self.num = Item.num
        self.name = item['name']
        self.price = item['price']
        self.power = item['power']
        self.grade = 'C'

    def printProduct(self):
        print(f"번호\t: {self.num}")
        print(f"아이템명\t: {self.name}")
        print(f"가격\t: {self.price}")
        print(f"공격력\t: {self.power}")
        print(f"등급\t: {self.grade}")
        print('===================')