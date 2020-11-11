'''
product 클래스
제품번호 / 제품명 / 가격 / 수량

추가
검색(제품번호)
수정(제품번호)
삭제(제품번호)
전체목록

'''


class Product:
    num = 0
    def __init__(self, pro_name, price, amount):
        Product.num+=1
        self.pro_num = Product.num
        self.pro_name = pro_name
        self.price = price
        self.amount = amount

    def printProduct(self):
        print('pro_num:', self.pro_num)
        print('pro_name:', self.pro_name)
        print('price:', self.price)
        print('amount:', self.amount)
        print('=============')


class Service:
    def __init__(self):
        self.dao = Dao()

    def addProduct(self):
        pro_name = input('제품명:')
        price = int(input('가격:'))
        amount = int(input('수량:'))

        item = Product(pro_name, price, amount)
        self.dao.insert(item)

    def selectProduct(self):
        pro_num = int(input('검색할 제품번호:'))
        info = self.dao.select(pro_num)
        info.printProduct()
        # print('')

    def updateProduct(self):
        pro_num = int(input('수정하려는 제품번호:'))
        price = int(input('수정할 가격:'))
        amount = int(input('수정할 수량:'))
        success = self.dao.update(pro_num, price, amount)
        if (success):
            print('수정되었습니다.')
        else:
            print('수정 실패')

    def deleteProduct(self):
        pro_num = int(input('삭제하려는 제품번호:'))
        success = self.dao.delete(pro_num)
        if (success):
            print('삭제되었습니다.')
        else:
            print('삭제 실패')

    def selectAll(self):
        all = self.dao.selectAll()
        for i in all:
            i.printProduct()


class Dao:
    def __init__(self):
        self.datas = []

    def insert(self, product):
        self.datas.append(product)

    def select(self, pro_num):
        for (idx, i) in enumerate(self.datas):
            if i.pro_num == pro_num:
                return self.datas[idx]

    def update(self, pro_num, price, amount):
        for (idx, i) in enumerate(self.datas):
            if i.pro_num == pro_num:
                self.datas[idx].price = price
                self.datas[idx].amount = amount
                return True
        return False

    def delete(self, pro_num):
        for (idx, i) in enumerate(self.datas):
            if i.pro_num == pro_num:
                del self.datas[idx]
                return True
        return False

    def selectAll(self):
        return self.datas


def main():
    service = Service()
    while True:
        sel = int(input('1.추가 2.검색 3.수정 4.삭제 5.전체목록 0.종료'))
        if sel == 1:
            service.addProduct()

        elif sel == 2:
            service.selectProduct()
        elif sel == 3:
            service.updateProduct()
        elif sel == 4:
            service.deleteProduct()
        elif sel == 5:
            service.selectAll()


main()
