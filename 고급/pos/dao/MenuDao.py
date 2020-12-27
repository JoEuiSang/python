import pymysql
from 고급.pos.dto.MenuDto import MenuDto


class MenuDao:
    def __init__(self):
        pass

    def connect(self):
        return pymysql.connect(host='localhost', user='jes', password='0000',
                               db='pypos', charset='utf8')

    def insertMenu(self, name, price, kind):
        conn = self.connect()
        sql = 'insert into menu(menuname, kind, price) values(%s,%s,' + price + ')'
        print(sql)
        cursor = conn.cursor()  # 사용할 커서 객체 생성
        param = (name, kind)
        cursor.execute(sql, param)
        conn.commit()  # 쓰기 완료
        conn.close()

    def updateMenu(self, id, name, price, kind, stock):
        conn = self.connect()
        sql = 'update menu set menuname = %s, price =' + price + ',kind = %s, stock = ' + stock + ' where menuid =' + str(
            id)
        print(sql)
        cursor = conn.cursor()  # 사용할 커서 객체 생성
        param = (name, kind)
        cursor.execute(sql, param)
        conn.commit()  # 쓰기 완료
        conn.close()

    def deleteMenu(self, id):
        conn = self.connect()
        sql = 'delete from menu where menuid =' + str(id)
        print(sql)
        cursor = conn.cursor()  # 사용할 커서 객체 생성
        cursor.execute(sql)
        conn.commit()  # 쓰기 완료
        conn.close()

    def selectAll(self):
        conn = self.connect()
        sql = 'select * from menu'
        cursor = conn.cursor()  # 사용할 커서 객체 생성
        cursor.execute(sql)  # sql실행. 실행한 결과는 cursor 객체에 담아
        datas = []
        for row in cursor:  # 검색된 결과를 한 줄씩 추출
            datas.append(MenuDto(row[0], row[1], row[2], row[3], row[4]))
        conn.close()
        return datas
