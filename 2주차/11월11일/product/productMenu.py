import product.productSvc as svc

class productMenu:
    def __init__(self):
        self.svc = svc.ServiceSvc()

    def run(self):
        while True:
            sel = int(input('1.추가 2.검색 3.수정 4.삭제 5.전체목록 0.종료'))
            if sel == 1:
                self.svc.addProduct()
            elif sel == 2:
                self.svc.selectProduct()
            elif sel == 3:
                self.svc.updateProduct()
            elif sel == 4:
                self.svc.deleteProduct()
            elif sel == 5:
                self.svc.selectAll()
            elif sel == 0:
                break