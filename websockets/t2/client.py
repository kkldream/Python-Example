import socket

HOST = '192.168.1.10'
PORT = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    cmd = input('Please input msg:')
    s.send(cmd.encode())
    data = s.recv(10)
    for i in range(10):
        print(data[i])
    print(f'server send: {data.decode()}')