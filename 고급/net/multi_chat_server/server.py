import threading, socket



class Room:  # 채팅방 클래스
    # class 변수 / static 변수 : 모든 객체가 공유
    ip = '192.168.35.99'
    port = 5555

    def __init__(self):
        self.client_soc = []  # 클라이언트와 1:1 통신할 소켓

    def addClient(self, c):
        self.client_soc.append(c)

    def delClient(self, c):
        self.client_soc.remove(c)

    def sendMsgAll(self, msg):
        for i in self.client_soc:
            i.sendMsg(msg)

class ChatClient:  # 텔레마케터
    def __init__(self, room, soc):
        self.room = room  # 채팅방, room 객체
        self.id = None  # 사용자 id
        self.soc = soc  # 사용자와 1:1 통신할 소켓

    def readMsg(self):
        self.id = self.soc.recv(1024).decode()
        while True:
            msg = self.soc.recv(1024).decode()
            if msg == '/stop':
                self.soc.sendall(msg.encode())
                self.room.delClient(self)
                break

            rmsg = self.id + ": " + msg
            rmsg = rmsg.encode(encoding='utf-8')
            self.room.sendMsgAll(self.id + ": " + msg)

        rmsg = self.id + "님이 퇴장했습니다"
        rmsg = rmsg.encode(encoding='utf-8')
        self.room.sendMsgAll(rmsg)

class ChatServer:
    # class 변수 / static 변수 : 모든 객체가 공유
    ip = '192.168.35.99'
    port = 5555

    def __init__(self):
        self.server_soc = None  # 서버 소켓(대문)
        self.room = Room()

    def open(self):
        self.server_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_soc.bind((ChatServer.ip, ChatServer.port))
        self.server_soc.listen()

    def run(self):
        self.open()
        print('서버 시작')
        while True:
            client_soc, addr = self.server_soc.accept()  # 클라이언트 1명만 받겠다는 의미
            c = ChatServer(self.room, client_soc)
            self.room.addClient(c)
            th = threading.Thread(target=c.readMsg)
            th.start()
            
        self.server_soc.close()

    def readMsg(self):
        self.id = self.soc.recv(1024).decode()
        self.room.sendMsgAll(self.id + '님이 입장하셨습니다')

        while True:
            msg = self.soc.recv(1024).decode()
            if msg == '/stop':
                self.soc.sendall(msg.encode())
                self.room.delClient(self)
                break

            rmsg = self.id + ": " + msg
            rmsg = rmsg.encode(encoding='utf-8')
            self.room.sendMsgAll(self.id + ": " + msg)

        self.room.sendMsgAll(self.id + "님이 퇴장했습니다")

    def sendMsg(self,msg):
        self.soc.sendall(msg.encode(encoding='utf-8'))

def main():
    server = ChatServer()
    server.run()


main()