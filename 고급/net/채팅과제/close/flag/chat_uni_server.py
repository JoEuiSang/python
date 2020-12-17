import threading, socket,time


class UniServer:
    # class 변수 / static 변수 : 모든 객체가 공유
    ip = '192.168.35.99'
    port = 5555
    SEND_STOP_FLAG = False
    RECV_STOP_FLAG = False

    def __init__(self):
        self.server_soc = None  # 서버 소켓(대문)
        self.client_soc = None  # 클라이언트와 1:1 통신할 소켓

    def open(self):
        self.server_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_soc.bind((UniServer.ip, UniServer.port))
        self.server_soc.listen()

    def sendMsg(self):  # 키보드 입력 받아 상대방에게 메시지 전송
        while True:
            msg = input('msg : ')
            sendMsg = msg.encode(encoding='utf-8')
            try:
                self.client_soc.sendall(sendMsg)
            except:
                break
            if msg == '/stop' :
                UniServer.SEND_STOP_FLAG = True
                break

    def sendStop(self, msg):
        sendMsg = msg.encode(encoding='utf-8')
        self.conn_soc.sendall(sendMsg)

    def recvMsg(self):  # 상대방이 보낸 메시지 읽어서 화면에 출력
        while True:
            try:
                data = self.client_soc.recv(1024)
            except:
                break
            msg = data.decode()
            print('상대방(클라) : ', msg)
            if msg == '/stop' :
                UniServer.RECV_STOP_FLAG = True
                self.sendStop('/stop')
                break

    def run(self):
        self.open()
        self.client_soc, addr = self.server_soc.accept()  # 클라이언트 1명만 받겠다는 의미
        print(addr)
        th1 = threading.Thread(target=self.sendMsg)
        th2 = threading.Thread(target=self.recvMsg)
        th3 = threading.Thread(target=self.recvMsg)

        th1.start()
        th2.start()
        th3.start()

    def close(self):
        self.client_soc.close()
        self.server_soc.close()
        print('서버 종료되었습니다')

    def shutThread(self):
        while True:
            if UniServer.RECV_STOP_FLAG == True and UniServer.SEND_STOP_FLAG == True:
                self.close()
                break

def main():
    server = UniServer()
    server.run()


main()