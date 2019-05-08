import socket
import sys
class HttpServer():
    def __init__(self,port,app):
        self.port = port
        self.s_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.s_socket.bind(("",port))
        self.s_socket.listen(5)
        self.response_data = None
        self.app = app

    def handler(self,c_s_socket):
        while True:
            c_s_socket,addr = self.s_socket.accept()
            data = c_s_socket.recv(1024).decode()
            ret = data.split("\r\n")[0].split(" ")

            try :
                request_path = ret[1]
            except:
                request_path = 'index'

            environ = {'path':request_path}
            if request_path.endswith(".py"):
                responsebody = self.app(environ,self.start_response)
                data = self.response_data+responsebody
                c_s_socket.send(data.encode('gbk'))
                c_s_socket.close()
            else:
                pass
                #静态服务器
    def start_response(self,status,header_list):
        first_line = 'HTTP/1.1 %s \r\n'%status
        response_header=''
        for key,value in header_list:
            response_header+=('%s:%s\r\n'%(key,value))
        self.response_data = first_line+response_header+'\r\n'
if __name__ == '__main__':
    try:
        port = int(sys.argv[1])
        model_name = sys.argv[2]
        app_name = sys.argv[3]
    except:
        port = 8888
        model_name = 'application'
        app_name = 'app'
    finally:
        kj  =__import__(model_name)
        app = getattr(kj,app_name)
        s_obj = HttpServer(port,app)
        s_obj.handler(s_obj)
