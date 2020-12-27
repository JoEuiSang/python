class productDao:
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