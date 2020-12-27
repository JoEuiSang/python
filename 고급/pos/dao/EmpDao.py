import pymysql
from 고급.pos.dto.EmpDto import EmpDto


class EmpDao:
    def __init__(self):
        pass

    def connect(self):
        return pymysql.connect(host='localhost', user='jes', password='0000',
                               db='pypos', charset='utf8')

    def insertEmp(self, name, pw, pCode):
        conn = self.connect()
        sql = 'insert into emp(name, pw, positionCode) values(%s,%s,' + pCode + ')'
        print(sql)
        cursor = conn.cursor()  # 사용할 커서 객체 생성
        param = (name, pw)
        cursor.execute(sql, param)
        conn.commit()  # 쓰기 완료
        conn.close()

    def updateEmp(self, id, name, pw, pCode):
        conn = self.connect()
        sql = 'update emp set name = %s, pw = %s, positionCode ='+ pCode +' where empid =' + str(id)
        print(sql)
        cursor = conn.cursor()  # 사용할 커서 객체 생성
        param = (name, pw)
        cursor.execute(sql, param)
        conn.commit()  # 쓰기 완료
        conn.close()

    def deleteEmp(self, id):
        conn = self.connect()
        sql = 'delete from emp where empid =' + str(id)
        print(sql)
        cursor = conn.cursor()  # 사용할 커서 객체 생성
        cursor.execute(sql)
        conn.commit()  # 쓰기 완료
        conn.close()

    def selectAll(self):
        conn = self.connect()
        sql = 'select e.empid, e.name, p.positionName from emp e, positiontb p where e.positionCode = p.positionCode order by e.positionCode, e.empid'
        cursor = conn.cursor()  # 사용할 커서 객체 생성
        cursor.execute(sql)  # sql실행. 실행한 결과는 cursor 객체에 담아
        datas = []
        for row in cursor:  # 검색된 결과를 한 줄씩 추출
            datas.append(EmpDto(row[0], row[1], row[2]))
        conn.close()
        return datas
