import os
import socket


class UploadClient:
    ip = '192.168.35.99'
    port = 5555
    path = './upFile/'

    def __init__(self):
        self.client_soc = None

    def conn(self):
        self.client_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_soc.connect((UploadClient.ip, UploadClient.port))

    def run(self):
        self.conn()
        flist = os.listdir(UploadClient.path)

        for idx, i in enumerate(flist):
            print(idx, ':', i)

        num = int(input('업로드할 파일의 번호를 입력하시오'))
        if 0 <= num < len(flist):
            f_name = flist[num]
            f = open(UploadClient.path+f_name, 'r', encoding='utf-8')
            f_cont = f.read()
            f.close()
            self.client_soc.sendall(f_name.encode(encoding='utf-8'))
            self.client_soc.sendall(f_cont.encode(encoding='utf-8'))


def main():
    uc = UploadClient()
    uc.run()


main()
