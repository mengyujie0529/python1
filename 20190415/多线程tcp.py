'''tcp服务端'''
import socket
import threading


def send(service_client_socket):
    try:
        while True:
            sendinfo = input("输入:")
            service_client_socket.send(sendinfo.encode("gbk"))
    except Exception as e:
        print(e)
    finally:

        tcp_socket.close()

def res(service_client_socket):
    try:
        while True:
            data = service_client_socket.recv(1024)
            if data:
                print(data.decode("gbk"))
            else:
                break
    except Exception as e:
        print(e)
    finally:
        service_client_socket.close()

if __name__ == '__main__':
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    tcp_socket.bind(("", 9999))
    tcp_socket.listen(5)

    while True:
        service_client_socket, client_addr = tcp_socket.accept()

        r_threading = threading.Thread(target=send,args=(service_client_socket,))
        c_threading = threading.Thread(target=res,args=(service_client_socket,))

        r_threading.start()
        c_threading.start()

        r_threading.join()
        c_threading.join()

