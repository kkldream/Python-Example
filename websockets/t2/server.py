import time
from SocketTCP import SocketTCP

host = '0.0.0.0'
port = 8217

def socket_listen(event, recv):
    if event == SocketTCP.CONNECTED:
        socket_client.send(f'connected {socket_client.addr}')
        print('socket_connected')
    elif event == SocketTCP.DISCONNECT:
        print('socket_disconnect')
        socket_client.connect()
        socket_client.waitConnect()
    else:
        print(f'socket_listen: {recv}')

if __name__ == '__main__':
    print('start')
    socket_client = SocketTCP(host, port)
    socket_client.set_listen(socket_listen)
    try:
        socket_client.connect()
        socket_client.waitConnect()
        while True:
            msg = str(time.time())
            socket_client.send(msg + '\n')
            print(msg)
            time.sleep(2)
    except KeyboardInterrupt:
        print('\nKeyboardInterrupt')
    finally:
        socket_client.close()
        print('finally')