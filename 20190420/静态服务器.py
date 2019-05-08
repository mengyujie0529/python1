'''这个程序实现的是一个静态服务器'''
import socket
import threading

'''主函数，实现逻辑'''
#套接字
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#删除端口
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
#绑定端口
server_socket.bind(('',8002))
#实时接收
server_socket.listen()
def main():#接收到网页传来的信息
    while True:
        handler_socket,address = server_socket.accept()
        data = handler_socket.recv(1024)#接收到的信息，最大为1024
        # print(data)
        request_datas = data.splitlines()#输出接收到的信息，并把他分割成每列输出，就为了方便我们看，如果直接打印出来的话就是一大串连续的，不好看
        for line in request_datas:
            print(line)


        '''
        格式：
        HTTP/1.1 状态码 说明\r\n　　#HTTP/1.1是指遵循HTTP的1.1版本协议，切记每一条后面都要加一个\r\n
        Headername1:header_value\r\n  #这里写的是说明，具体可以打开网页'www.baidu.com'（推荐用Google Chrome）按ｆ12然后在Network里边按Doc,然后刷新页面，点击Name里面的'www.baidu.com',选第一个'Headers'再点击'Response Headers'里可以借鉴,不过每一段后面记得都加一个\r\n
        Headername2:header_value\r\n
        Headername3:header_value\r\n
        \r\n       #状态码和说明写完后一定要单独返回一个\r\n
        Response_body ＃响应体，就是数据，网页、图片、文本
        '''
        response_Header = 'HTTP/1.1 200 ok\r\n'
        response_name = 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0\r\n'+'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'+'Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2'+'Accept-Encoding: gzip, deflate'+'Connection: keep-alive'+'Upgrade-Insecure-Requests: 1'

        # responseHeader += '\r\n'
        response_name += '\r\n'
        response_body = 'hello world!'
        reponse = response_Header+response_name+response_body
        handler_socket.send(reponse.encode('utf-8'))



if __name__ == '__main__':
    main_thread = threading.Thread(target=main)
    main_thread.start()#想要连接这个静态服务器，只能用浏览器连接（输入网址的地方直接输入：　＇你设置的ｉｐ地址＇：＇端口＇比如：192.168.58.137：8002）