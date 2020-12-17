import threading, socket


class UniClient:
    # class 변수 / static 변수 : 모든 객체가 공유
    ip = '192.168.35.99'
    port = 5555
    STOP_FLAG = False

    def __init__(self):
        self.conn_soc = None  # 서버와 연결된 소켓

    def conn(self):
        self.conn_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn_soc.connect((UniClient.ip, UniClient.port))

    def sendMsg(self):  # 키보드 입력 받아 상대방에게 메시지 전송
        while True:
            msg = input('msg : ')
            sendMsg = msg.encode(encoding='utf-8')
            try:
                self.conn_soc.sendall(sendMsg)
            except:
                break
            if msg == '/stop' or UniClient.STOP_FLAG == True:
                UniClient.STOP_FLAG = True
                break
        self.close()

    def sendStop(self, msg):
        sendMsg = msg.encode(encoding='utf-8')
        try:
            self.conn_soc.sendall(sendMsg)
        except:
            pass
        self.close()

    def recvMsg(self):  # 상대방이 보낸 메시지 읽어서 화면에 출력
        while True:
            try:
                data = self.conn_soc.recv(1024)
            except:
                break
            recvMsg = data.decode()
            print('상대방(서버) : ', recvMsg)
            if recvMsg == '/stop' or UniClient.STOP_FLAG == True:
                UniClient.STOP_FLAG = True
                break
        self.sendStop('/stop')

    def run(self):
        self.conn()

        th1 = threading.Thread(target=self.sendMsg)
        th2 = threading.Thread(target=self.recvMsg)

        th1.start()
        th2.start()

    def close(self):
        self.conn_soc.close()
        print('클라이언트 종료되었습니다')


def main():
    conn = UniClient()
    conn.run()


main()
