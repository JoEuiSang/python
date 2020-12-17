import threading, time

def f1(num):
    for i in range(1, 21):
        print('th'+num+':', i)
        time.sleep(0.3) #실행중인 현재 쓰레드를 초만큼 잠재움, 딜레이  #인자값에 따라서 제어가능

def f2():
    s = 'abcdefghijklmnopqrstuvwxyz'
    for i in s:
        print('th4 : ', i)
        time.sleep(0.3)

def main():
    #스레드를 생성하는 코드 , target : 스레드가 실행할 함수, args : target함수에 파라메터 절달, 없으면 생략 가능
    th1 = threading.Thread(target=f1, args=('1'))
    th2 = threading.Thread(target=f1, args=('2'))
    th3 = threading.Thread(target=f1, args=('3'))
    th4 = threading.Thread(target=f2, args=())

    th1.start()
    th2.start()
    th3.start()
    th4.start()

    for i in range(100, 140, 2):  #메인 쓰레드
        print('main : ', i)
        time.sleep(0.3)

main()
