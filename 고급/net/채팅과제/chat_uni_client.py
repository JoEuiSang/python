import threading, socket


class UniClient:
    # class 변수 / static 변수 : 모든 객체가 공유
    ip = 'localhost'
    port = 5555

    def __init__(self):
        self.conn_soc = None  # 서버와 연결된 소켓

    def conn(self):
        self.conn_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn_soc.connect((UniClient.ip, UniClient.port))

    def sendMsg(self):  # 키보드 입력 받아 상대방에게 메시지 전송
        while True:
            msg = input('msg : ')
            msg = msg.encode(encoding='utf-8')
            self.conn_soc.sendall(msg)
            if msg == '/stop':
                # self.close()
                break

    def recMsg(self):  # 상대방이 보낸 메시지 읽어서 화면에 출력
        while True:
            msg = self.conn_soc.recv(1024)
            msg = msg.decode()
            print('상대방(서버) : ', msg)
            if msg == '/stop':
                self.close()
                break

    def run(self):
        self.conn()

        th1 = threading.Thread(target=self.sendMsg)
        th2 = threading.Thread(target=self.recMsg)

        th1.start()
        th2.start()

    def close(self):
        self.conn_soc.close()
        print('종료되었습니다')


def main():
    conn = UniClient()
    conn.run()


main()