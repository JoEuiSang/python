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
        img = open('new1.jpg','wb')

        imgData = self.client_soc.recv(1024)
        while imgData:
            img.write(imgData)
            imgData = self.client_soc.recv(1024)
        img.close()
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
