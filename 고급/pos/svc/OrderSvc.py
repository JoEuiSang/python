import 고급.pos.dao.OrderDao as oDao


class OrderSvc:
    def __init__(self):
        self.dao = oDao.OrderDao()

    def addOrder(self, msg):
        orderMenu = msg
        print('ordermenu:',orderMenu)
        self.dao.updateStock(orderMenu)

