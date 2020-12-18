from 고급.db.게시판.board import BoardService
from 고급.db.게시판.loginInfo import Session
from 고급.db.게시판.member import MemberService


def main():
    memSvc = MemberService()
    brdSvc = BoardService()

    while True:
        if Session.id == '':
            print('1.회원 관리\n2.게시판\n3.종료')
        elif Session.id != '':
            print(Session.id+'님 접속')
            print('1.회원 관리\n2.게시판\n3.종료')

        sel= input()
        if sel == '1':
            memSvc.memMain()
        elif sel == '2':
            brdSvc.brdMain()
        elif sel == '3':
            break

main()