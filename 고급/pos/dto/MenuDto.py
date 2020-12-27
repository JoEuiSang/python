class MenuDto:
    def __init__(self, id=None, menuName=None, price=None, kind=None, stock=None):
        self.id = id
        self.name = menuName
        self.price = price
        self.kind = kind
        self.stock = stock

    def __str__(self):
        return '메뉴번호 : '+ str(self.id)+', 메뉴명 : '+self.name+', 가격 : '+str(self.price)+', 종류 : '+self.kind+', 재고 : '+str(self.stock)