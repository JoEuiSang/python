import product.productDao as dao
import product.productVo as vo

class ServiceSvc:
    def __init__(self):
        self.dao = dao.productDao()

    def addProduct(self):
        pro_name = input('제품명:')
        price = int(input('가격:'))
        amount = int(input('수량:'))

        item = vo.ProductVo(pro_name, price, amount)
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