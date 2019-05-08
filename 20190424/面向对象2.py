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
            data=c_s_socket.recv(1024).decode()
            ret = data.split("\r\n")
            for i in ret:
                print(i)
            first_line = ret[0]
            ret1 = first_line.split(" ")
            print(ret1)
            try:
                path = ret1[1]
            except:
                path = "/"

            if path == "/":
                status = "200 ok"
                with open("index.html","rb") as f:
                    responsebody = f.read()
            elif path == "/pic":
                status = "200 ok"
                with open("a.jpg","rb") as f:
                    responsebody = f.read()
            else:
                status = "404 no ok"
                with open("err.html","rb")as f:
                    responsebody = f.read()
            fl = "HTTP/1.1 " + status +"\r\n"
            fl += "name:server\r\n"
            fl+="\r\n"
            response = fl.encode("gbk")+responsebody
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