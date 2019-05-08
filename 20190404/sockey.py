import socket

if __name__ == '__main__':
    #1.创建UDP的客户端,创建套接字
    #第一个参数表示的是地址类型，用于Internet之间的通信
    #第二个参数表示的是传输协议udp
    udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    #2.使用套接字进行收发数据
    #第一个参数表示发送的信息，第二个参数表示地址
    udp_socket.sendto("difjsdlksmg ".encode("utf-8"), ('192.168.78.128',8080))
    udp_socket.sendto("1233456".encode("utf-8"), ('192.168.58.1', 8080))
    #3.关闭套接字
    udp_socket.close()