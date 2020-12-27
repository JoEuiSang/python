import 고급.pos.socket.Client as cnt
import 고급.pos.socket.Server as sv
import threading


def main():
    server = sv.KioskServer()
    th1 = threading.Thread(target=server.run)
    th1.start()

    clientTh = []
    kioskList = []
    connCnt=0

    while True:
        print('1.매장관리\n2.주문하기\n0.종료')
        sel = input()
        if sel == '1':
            print('매장관리')
        elif sel == '2':
            print('주문하기')
            kioskList.append(cnt.KioskClient())
            clientTh.append(threading.Thread(target=kioskList[connCnt].run))
            clientTh[connCnt].start()
            connCnt+=1


main()
