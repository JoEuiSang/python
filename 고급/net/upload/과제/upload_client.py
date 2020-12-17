import os
import socket
import threading


class UploadClient:
    ip = '192.168.35.99'
    port = 5556
    clientPath = './clientFolder/'\

    def __init__(self):
        self.client_soc = None

    def conn(self):
        self.client_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_soc.connect((UploadClient.ip, UploadClient.port))

    def download(self):
        while True:
            yn = input('다운로드하시겠습니까? Y/N')
            if yn == 'y' or yn =='Y' :
                yn = yn.encode()
                self.client_soc.sendall(yn)     # 다운여부 전송
                flist = self.client_soc.recv(1024) # 파일 목록 수신
                flist = flist.decode().split(',')
                for idx, i in enumerate(flist):
                    print(idx, ':', i)
                num = int(input('다운로드할 파일의 번호를 입력하시오'))
                if 0 <= num < len(flist):
                    self.client_soc.sendall(str(num).encode()) #다운로드파일번호 전송
                    f_cont = self.client_soc.recv(1024) #파일내용 수신
                    f_cont = f_cont.decode()
                    print(f_cont)
                    fileName = input('저장할 파일이름:')
                    f = open(UploadClient.clientPath + fileName, 'w', encoding='utf-8')
                    f.write(f_cont)
                    f.close()
            else:
                self.client_soc.sendall('stop'.encode()) # 다운여부 전송
                print('종료합니다')
                break

        self.client_soc.close()

    def run(self):
        self.conn()
        print(self.client_soc)
        th1 = threading.Thread(target=self.download)

        th1.start()


def main():
    uc = UploadClient()
    uc.run()


main()
