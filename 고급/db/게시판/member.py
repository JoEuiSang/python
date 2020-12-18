import pymysql

from 고급.db.게시판.loginInfo import Session


class MemberVo:
    def __init__(self, id, name, pwd, email):
        self.id = id
        self.email = email
        self.name = name
        self.pwd = str(pwd)

    def __str__(self):
        return 'id:' + self.id + ' / name:' + self.name + ' / pwd:' + self.pwd + ' / email:' + self.email


class MemberService:
    def __init__(self):
        self.dao = MemberDao()

    def memMain(self):
        while True:
            print('1.가입\n2.로그인\n3.로그아웃\n4.내정보수정\n5.탈퇴\n6.뒤로가기')
            sel = input()
            if sel == '1':
                self.addMember()
            elif sel == '2' and Session.id == '':
                self.login()
            elif sel == '3' and Session.id != '':
                self.logout()
            elif sel == '4' and Session.id != '':
                self.editMember()
            elif sel == '5' and Session.id != '':
                self.removeMember()
            elif sel == '6':
                break

    def removeMember(self):
        print('회원탈퇴')
        result = self.dao.deleteMember(Session.id)
        if result is not None:
            print('탈퇴 성공')
            Session.id=''
        else:
            print('탈퇴 실패')

    def editMember(self):
        print('정보 수정')
        name = input('수정할 이름:')
        result = self.dao.updateMember(Session.id, name)
        print(result)
        if result == 1:
            print('수정 성공')
        else:
            print('수정 실패')

    def login(self):
        print('로그인')
        id = input('id:')
        pw = input('pw:')
        result = self.dao.login(id, pw)

        if result is not None:
            print('로그인 성공', result[0])
            Session.id = result[0]
        else:
            print('id 또는 pw를 확인해주세요')

    def logout(self):
        Session.id = ''
        print('로그아웃 되었습니다')

    def selectAll(self):
        datas = self.dao.selectAll()
        for i in datas:
            print(i)

    def addMember(self):
        print('회원가입')
        id = input('id:')
        name = input('name:')
        pwd = input('pwd:')
        email = input('email:')
        p = self.dao.insertMember(MemberVo(id, name, pwd, email))
        if p is not None:
            print('가입완료')
        else:
            print('가입실패')


class MemberDao:
    def connect(self):
        return pymysql.connect(host='localhost', user='jes', password='0000',
                               db='pytest', charset='utf8')

    def deleteMember(self, id):
        conn = self.connect()
        sql = 'delete from member where id = %s'
        cursor = conn.cursor()  # 사용할 커서 객체 생성
        cursor.execute(sql, id)  # sql실행. 실행한 결과는 cursor 객체에 담아
        conn.commit()
        conn.close()
        print(cursor)
        return cursor.rowcount

    def updateMember(self, id, name):
        conn = self.connect()
        sql = 'update member set name = %s where id = %s'
        cursor = conn.cursor()  # 사용할 커서 객체 생성
        d = (name, id)
        cursor.execute(sql, d)  # sql실행. 실행한 결과는 cursor 객체에 담아
        conn.commit()
        conn.close()
        return cursor.rowcount

    def login(self, id, pw):
        conn = self.connect()
        sql = 'select * from member where id = %s and pwd = %s'
        cursor = conn.cursor()  # 사용할 커서 객체 생성
        d = (id, pw)
        cursor.execute(sql, d)  # sql실행. 실행한 결과는 cursor 객체에 담아
        print(cursor)
        row = cursor.fetchone()  # 검색 결과 한줄추출
        return row

    def getMember(self, id):
        conn = self.connect()
        sql = 'select * from member where id = %s'
        cursor = conn.cursor()  # 사용할 커서 객체 생성
        cursor.execute(sql, id)  # sql실행. 실행한 결과는 cursor 객체에 담아

        return cursor.rowcount

    def selectAll(self):
        conn = self.connect()
        sql = 'select * from member'
        cursor = conn.cursor()  # 사용할 커서 객체 생성
        cursor.execute(sql)  # sql실행. 실행한 결과는 cursor 객체에 담아
        datas = []
        for row in cursor:  # 검색된 결과를 한 줄씩 추출
            datas.append(MemberVo(row[0], row[1], row[2], row[3]))
        conn.close()
        return datas

    def insertMember(self, m):
        conn = self.connect()
        sql = 'insert into member(id, name, pwd, email) values(%s, %s, %s, %s)'
        cursor = conn.cursor()  # 사용할 커서 객체 생성
        d = (m.id, m.name, m.pwd, m.email)
        cursor.execute(sql, d)
        conn.commit()  # 쓰기 완료
        conn.close()
        return self.getMember(m.id)
