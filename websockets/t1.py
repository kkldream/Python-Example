import socket
BUFSIZE=4096
tcpServerSocket=socket.socket()#创建socket对象
hostname= socket.gethostname()#获取本地主机名
sysinfo = socket.gethostbyname_ex(hostname)
hostip='192.168.1.10'
port=7000#设置端口
tcpServerSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)#让端口可以复用
tcpServerSocket.bind((hostip,port))#将地址与套接字绑定，且套接字要求是从未被绑定过的
tcpServerSocket.listen(5)#代办事件中排队等待connect的最大数目
while True:
    print("等待连接")
    #建立客户端连接,接受connection，返回两个参数，c是该connection上可以发送和接收数据的新套接字对象
    #addr是与connection另一端的套接字绑定的地址
    clientSocket, addr = tcpServerSocket.accept()  
    print ('连接地址：', addr)
    while True:
        data=clientSocket.recv(BUFSIZE).decode()
        if not data:
            break
        #向客户端表示接收到数据
        str='来自服务端的消息！'
        clientSocket.send(str.encode())#字符串编码为字节
    #套接字在垃圾收集garbage-collected时会自动close
    #close关闭该connection上的资源但不一定马上断开connection
    #想要立即断开connection，要先调用shutdown再close
    clientSocket.close() # 关闭连接
tcpServerSocket.close()