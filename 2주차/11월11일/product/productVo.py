class ProductVo:
    num = 0
    def __init__(self, pro_name, price, amount):
        ProductVo.num+=1
        self.pro_num = ProductVo.num
        self.pro_name = pro_name
        self.price = price
        self.amount = amount

    def printProduct(self):
        print('pro_num:', self.pro_num)
        print('pro_name:', self.pro_name)
        print('price:', self.price)
        print('amount:', self.amount)
        print('=============')