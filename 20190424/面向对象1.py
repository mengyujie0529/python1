import socket
import sys
class HttpServer():
    def __init__(self,port):
        self.server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server_socket.bind(("",port))
        self.server_socket.listen(5)
    def handler(self,c_s_socket):
        while True:
            c_s_socket,addr = self.server_socket.accept()
            data = c_s_socket.recv(1024).decode()
            ret1=data.split("\r\n")
            request_first_line = ret1[0]
            ret2=request_first_line.split(" ")
            # print(ret2)
            try:
                path = ret2[1]
            except:
                path = "/"
            if path == "/":
                status="200 OK"
                with open("index.html","rb") as f:
                    responsebody = f.read()
            elif path == "/pic":
                status = "200 OK"
                with open("a.jpg","rb") as f:
                    responsebody = f.read()
            else:
                status = "404 not found"
                with open("err.html","rb") as f:
                    responsebody = f.read()

            first_line = 'HTTP/1.1 '+status+'\r\n'
            first_line+='name:server\r\n'
            first_line+='\r\n'

            response = first_line.encode("GBK")+responsebody
            c_s_socket.send(response)
            c_s_socket.close()
if __name__ == '__main__':
    try:
        port = int(sys.argv[1])
    except:
        port = 8000
    finally:
        socket_obj = HttpServer(port)
        socket_obj.handler(socket_obj)