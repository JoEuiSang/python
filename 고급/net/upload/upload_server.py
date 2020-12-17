import threading, socket


class UploadServer:
    # class 변수 / static 변수 : 모든 객체가 공유
    ip = '192.168.35.99'
    port = 5555
    path = './upFile/'

    def __init__(self):
        self.server_soc = None  # 서버 소켓(대문)
        self.client_soc = None  # 클라이언트와 1:1 통신할 소켓

    def open(self):
        self.server_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_soc.bind((UploadServer.ip, UploadServer.port))
        self.server_soc.listen()

    def sendMsg(self):  # 키보드 입력 받아 상대방에게 메시지 전송
        while True:
            msg = input('msg : ')
            msg = msg.encode(encoding='utf-8')
            self.client_soc.sendall(msg)
            if msg == '/stop':
                break

    def recMsg(self):  # 상대방이 보낸 메시지 읽어서 화면에 출력
        while True:
            msg = self.client_soc.recv(1024)
            msg = msg.decode()
            print('상대방(클라) : ', msg)
            if msg == '/stop':
                # self.close()
                break

    def run(self):
        self.open()
        self.client_soc, addr = self.server_soc.accept()  # 클라이언트 1명만 받겠다는 의미
        # 1. 파일명 받아오기
        # 2. up 폴더에 받아온 파일명으로 파일 쓰기모드로 오픈
        # 3. 파일 내용 받기
        # 4. 2번에서 오픈한 파일에 내용 복사
        # 5. 파일 닫기

        f_name = self.client_soc.recv(1024)
        f_name = f_name.decode()
        f_cont = self.client_soc.recv(1024)
        f_cont = f_cont.decode()
        f = open('./newUp/'+f_name, 'w', encoding='utf-8')
        f.write(f_cont)
        f.close()

        self.client_soc.close()
        self.server_soc.close()

    def close(self):
        self.client_soc.close()
        self.server_soc.close()
        print('종료되었습니다')


def main():
    server = UploadServer()
    server.run()


main()