import socket, threading, time


def main():
    HOST = '192.168.35.99'
    PORT = 9999

    # 통신할 소켓 오픈
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 서버 accept()에 연결요청. server ip, port
    client_socket.connect((HOST, PORT))

    t1 = threading.Thread(target=send, args=(client_socket,))
    t2 = threading.Thread(target=recv, args=(client_socket,))
    t1.start()
    t2.start()

def send(client_socket):
    while True:
        msg = input('msg:')
        client_socket.sendall(msg.encode())


def recv(client_socket):
    while True:
        data = client_socket.recv(1024)
        msg = data.decode()
        print('\n서버 : ', msg, end='\n')


main()
