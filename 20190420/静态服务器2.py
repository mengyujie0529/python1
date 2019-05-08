'''静态服务器'''
import  socket

# 1.浏览器和服务器进行连接

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(("",5000))
server_socket.listen(5)
while True:
    # 2.在三次握手完成后，为客户端套接字创建客服

    c_s_socket,addressinfo = server_socket.accept()

    # 3.浏览器向服务器发送请求报文,服务器接收报文

    data = c_s_socket.recv(1024).decode()
    # print(data)
    #data是接收到的浏览器请求报文,并且是二进制文件
    ret = data.split("\r\n")
    for i in ret:
        print(i)

    # 4.服务器根据浏览器发送的报文返回具体响应
    #todo:开始拼接响应报文
    # todo:截取请求的路径，获取请求的具体内容，根据路径不同，返回不同数据
    # 4.0获取请求报文第一行
    request_first_line = ret[0]
    ret2=request_first_line.split(' ')
    print(ret2)
    try:
        request_path = ret2[1]
    except:
        request_path = '/index'
    # 根据路径，获得对应数据
    if request_path == '/index':
        status = '200 ok'
        with open('index.html','rb') as f:
            responsebody = f.read()
    elif request_path == '/login':
        status = '200 ok'
        with open('a.jpg','rb') as f:
            responsebody = f.read()
    else:
        status = '404 not found'
        with open('err.html','rb')as f:
            responsebody=f.read()


    # 4.1拼接第一行的数据HTTP/1.1 状态码 说明\r\n
    first_line = 'HTTP/1.1' + status +'\r\n'
    first_line+='name:server\r\n'
    first_line+='\r\n'
    # responsebody='hello world!'
    response = first_line.encode('GBK')+responsebody
    # c_s_socket.send(response)
    need_send = len(response)#需要发送的数据大小
    #已经发送的数据大小
    sent_count = 0
    while sent_count < need_send:
        #本次已经发送的数据大小
        count = c_s_socket.send(response[sent_count:])
        #已经发送的数据大小+=本次发送的数据大小
        sent_count += count

    # 5.人工客服完成任务之后被销毁
    c_s_socket.close()
    # 6.服务器套接字一把那不会关闭