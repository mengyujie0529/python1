'''此文件实现的是应用程序框架'''

import time
# WSGI接口
def app(environ,start_response):
    '''

    :param environ: 跟HTTP请求相关的数据（用户的请求路径，用户的请求头），字典
    :param start_response:函数引用（由服务器提供），作用：设置状态和响应头
    start_reponse这个方法：设置状态和响应头，这个函数有两个参数，
    第一个参数表示状态，第二个表示响应的头部（类型：列表），写在服务器上，但是框架上调用
    :return:
    '''
    # request_path = environ["path"]
    # if request_path == "/gett.py":
    # # print('environ:',environ)
    #     with open("ab.html","rb") as f:
    #         t =f.read()
    #     t = input("输入温度")
    #     start_response('200 ok',[('server','wsgisever'),('name','guazi'),('path',request_path)])
    #
    #     return "温度"+t
def gettime():
    time1=time.ctime()
    return time1
def score():
    count = 100
    html='''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>
    <h1>your score:%s</h1>
    
    </body>
    </html>
    '''%count
    return html

def app(environ,start_response):
    request_path = environ["path"]
    if request_path == "/gettime.py":

        start_response('200 ok',[('server','wsgisever'),('name','guazi'),('path',request_path)])
        time_data = gettime()
        return time_data
    elif request_path =="/score.py":
        start_response('200 ok', [('server', 'wsgisever'), ('name', 'guazi'), ('path', request_path)])
        scoredata = score()
        return scoredata