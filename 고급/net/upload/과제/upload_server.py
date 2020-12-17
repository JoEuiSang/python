import os
import threading, socket


class UploadServer:
    # class 변수 / static 변수 : 모든 객체가 공유
    ip = '192.168.35.99'
    port = 5556
    serverPath = './serverFolder/'

    def __init__(self):
        self.server_soc = None  # 서버 소켓(대문)
        self.client_soc = None  # 클라이언트와 1:1 통신할 소켓

    def open(self):
        self.server_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_soc.bind((UploadServer.ip, UploadServer.port))
        self.server_soc.listen()

    def giveFile(self):  # 키보드 입력 받아 상대방에게 메시지 전송
        while True:
            stop = self.client_soc.recv(1024) # 다운여부 수신
            print('?')
            stop = stop.decode()
            if stop == 'stop':
                break
            else:
                flist = os.listdir(UploadServer.serverPath)
                msg = ",".join(flist)
                self.client_soc.sendall(msg.encode()) # 파일 목록 전송
                print('파일 목록을 보여줬습니다')

                wantNum = self.client_soc.recv(1024) #다운로드파일번호 수신
                wantNum = wantNum.decode()

                flist = os.listdir(UploadServer.serverPath)
                fileName = flist[int(wantNum)]
                f = open(UploadServer.serverPath + fileName, 'r', encoding='utf-8')

                f_cont = f.read()
                print(f_cont)
                self.client_soc.sendall(f_cont.encode()) #파일 내용 전송
                f.close()

        self.close()

    def run(self):
        self.open()
        self.client_soc, addr = self.server_soc.accept()  # 클라이언트 1명만 받겠다는 의미
        print(addr)
        th1 = threading.Thread(target=self.giveFile)  # 클라이언트에 서버 파일 목록 보여주기
        th1.start()
        # 1. 파일명 받아오기
        # 2. up 폴더에 받아온 파일명으로 파일 쓰기모드로 오픈
        # 3. 파일 내용 받기
        # 4. 2번에서 오픈한 파일에 내용 복사
        # 5. 파일 닫기


    def close(self):
        self.client_soc.close()
        self.server_soc.close()
        print('종료되었습니다')


def main():
    server = UploadServer()
    server.run()


main()
