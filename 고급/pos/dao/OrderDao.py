import pymysql


class OrderDao:
    def __init__(self):
        pass

    def connect(self):
        return pymysql.connect(host='localhost', user='jes', password='0000',
                               db='pypos', charset='utf8')

    def updateStock(self, orderMenu):
        conn = self.connect()
        list = orderMenu.split(',')
        inSql = ''
        for idx, i in enumerate(list):
            if idx == 0:
                inSql += '\'' + i + '\''
            else:
                inSql += ',\'' + i + '\''

        print(inSql)

        sql = 'update menu m1, menu m2 set m1.stock = m2.stock-1 where m1.menuid = m2.menuid and m1.menuname in('+inSql+')'
        try:
            print(sql)
            cursor = conn.cursor()  # 사용할 커서 객체 생성
            cursor.execute(sql)
            conn.commit()  # 쓰기 완료
        except Exception as e:
            print(e)

        conn.close()

    # def updateStock(self, orderMenu):
    #     conn = self.connect()
    #     list = orderMenu.split(',')
    #     for m in list:
    #         print('m:',m)
    #         sql = 'update menu m1, menu m2 set m1.stock = m2.stock-1 where m1.menuid = m2.menuid and m1.menuname = %s'
    #         try:
    #             print(sql)
    #             cursor = conn.cursor()  # 사용할 커서 객체 생성
    #             cursor.execute(sql, m)
    #
    #         except Exception as e:
    #             print(e)
    #     conn.commit()  # 쓰기 완료
    #     conn.close()

