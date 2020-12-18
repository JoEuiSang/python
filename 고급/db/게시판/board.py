import pymysql

from 고급.db.게시판.loginInfo import Session


class BoardVo:
    def __init__(self, writer, title, content, num=None, w_date=None):
        self.content = content
        self.title = title
        self.writer = writer
        self.w_date = w_date
        self.num = num

    def __str__(self):
        return str(self.num) + ',' + self.writer + ',' + self.title + ',' + self.content + ',' + str(self.w_date)


class BoardDao:
    def connect(self):
        return pymysql.connect(host='localhost', user='jes', password='0000',
                               db='pytest', charset='utf8')

    def selectAll(self):
        conn = self.connect()
        sql = 'select * from 게시판'
        cursor = conn.cursor()  # 사용할 커서 객체 생성
        cursor.execute(sql)  # sql실행. 실행한 결과는 cursor 객체에 담아
        datas = []
        for row in cursor:  # 검색된 결과를 한 줄씩 추출
            # print(type(row[0]), type(row[1]), type(row[2]), type(row[3]), type(row[4]))
            # 0:num, 1:writer, 2:date, 3:title, 4:content
            # 생성자 1writer, 3title, 4content, 0num=None, 2w_date
            datas.append(BoardVo(row[1], row[3], row[4], row[0], row[2]))
        conn.close()
        return datas

    def insertBoard(self, b):
        conn = self.connect()
        sql = 'insert into 게시판(writer, title, content, w_date) values(%s, %s, %s, sysdate())'
        cursor = conn.cursor()  # 사용할 커서 객체 생성
        d = (b.writer, b.title, b.content)
        cursor.execute(sql, d)
        conn.commit()  # 쓰기 완료
        conn.close()

    def getBoard(self, id):
        conn = self.connect()
        sql = 'select * from 게시판 where writer = %s'
        cursor = conn.cursor()  # 사용할 커서 객체 생성
        cursor.execute(sql, id)  # sql실행. 실행한 결과는 cursor 객체에 담아
        datas = []
        for row in cursor:
            datas.append(BoardVo(row[1], row[3], row[4], row[0], row[2]))
        conn.close()
        return datas

    def getBoardById(self, id):
        conn = self.connect()
        sql = 'select * from 게시판 where writer like %s'
        wildCard = '%' + id + '%'
        cursor = conn.cursor()  # 사용할 커서 객체 생성
        cursor.execute(sql, wildCard)  # sql실행. 실행한 결과는 cursor 객체에 담아
        datas = []
        for row in cursor:
            datas.append(BoardVo(row[1], row[3], row[4], row[0], row[2]))
        conn.close()
        return datas

    def getBoardByTitle(self, title):
        conn = self.connect()
        sql = 'select * from 게시판 where title like %s'
        wildCard = '%' + title + '%'
        cursor = conn.cursor()  # 사용할 커서 객체 생성
        cursor.execute(sql, wildCard)  # sql실행. 실행한 결과는 cursor 객체에 담아
        datas = []
        for row in cursor:
            datas.append(BoardVo(row[1], row[3], row[4], row[0], row[2]))
        conn.close()
        return datas

    def getBoardByContent(self, content):
        conn = self.connect()
        sql = 'select * from 게시판 where content like %s'
        wildCard = '%' + content + '%'
        cursor = conn.cursor()  # 사용할 커서 객체 생성
        cursor.execute(sql, wildCard)  # sql실행. 실행한 결과는 cursor 객체에 담아
        datas = []
        for row in cursor:
            datas.append(BoardVo(row[1], row[3], row[4], row[0], row[2]))
        conn.close()
        return datas

    def updatePost(self, postNum, title, content):
        conn = self.connect()
        sql = 'update 게시판 set title = %s, content = %s where num = %s'
        cursor = conn.cursor()  # 사용할 커서 객체 생성
        d = (title, content, postNum)
        cursor.execute(sql, d)  # sql실행. 실행한 결과는 cursor 객체에 담아
        conn.commit()
        conn.close()
        return cursor.rowcount

    def deletePost(self, postNum):
        conn = self.connect()
        sql = 'delete from 게시판 where num = %s'
        cursor = conn.cursor()  # 사용할 커서 객체 생성
        cursor.execute(sql, postNum)  # sql실행. 실행한 결과는 cursor 객체에 담아
        conn.commit()
        conn.close()
        return cursor.rowcount


class BoardService:
    def __init__(self):
        self.dao = BoardDao()

    def brdMain(self):
        while True:
            print('1.게시판보기\n2.글쓰기\n3.글수정\n4.글삭제\n5.뒤로가기')
            sel = input()
            if sel == '1':
                while True:
                    print('1.전체보기\n2.아이디로검색\n3.제목으로검색\n4.내용으로검색\n5.뒤로가기')
                    search = input()
                    if search == '1':
                        self.selectAll()
                    elif search == '2':
                        self.searchId()
                    elif search == '3':
                        self.searchTitle()
                    elif search == '4':
                        self.searchContent()
                    elif search == '5':
                        break
            elif sel == '2' and Session.id != '':
                self.addBoard()
            elif sel == '3' and Session.id != '':
                self.editPost()
            elif sel == '4' and Session.id != '':
                self.delPost()
            elif sel == '5':
                break

    def selectAll(self):
        datas = self.dao.selectAll()
        print('<게시판>')
        for i in datas:
            print(i)

    def getPost(self, writer):
        datas = self.dao.getBoard(writer)
        print('<내가 쓴 게시글>')
        for i in datas:
            print(i)

    def searchId(self):
        writer = input('id입력:')
        datas = self.dao.getBoardById(writer)
        print(writer + '의 게시글>')
        for i in datas:
            print(i)

    def searchTitle(self):
        title = input('title입력:')
        datas = self.dao.getBoardByTitle(title)
        print(title + '을 포함한 제목의 게시글>')
        for i in datas:
            print(i)

    def searchContent(self):
        cont = input('content입력:')
        datas = self.dao.getBoardByContent(cont)
        print(cont + '을 포함한 내용의 게시글>')
        for i in datas:
            print(i)

    def addBoard(self):
        print('글쓰기')
        title = input('title:')
        content = input('content:')
        b = BoardVo(Session.id, title, content)
        print(b.writer, ',', b.title, ',', b.content)
        self.dao.insertBoard(b)

    def editPost(self):
        self.getPost(Session.id)
        postNum = input('수정할 글 번호 선택:')
        title = input('수정할 제목:')
        content = input('수정할 내용:')
        result = self.dao.updatePost(postNum, title, content)
        print(result)
        if result == 1:
            print('수정 성공')
        else:
            print('수정 실패')

    def delPost(self):
        self.getPost(Session.id)
        postNum = input('삭제할 글 번호 선택:')
        result = self.dao.deletePost(postNum)
        print(result)
        if result == 1:
            print('삭제 성공')
        else:
            print('삭제 실패')
