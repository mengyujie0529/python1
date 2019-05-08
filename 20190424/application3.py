'''此文件实现的是应用程序框架'''

import time
def gettime(func):
    def inner(*args):
        time_data = time.ctime()
        func(*args)
        return time_data
    return inner
# def score(func):
#     def inner(*args):
#         count = 100
#         html = '''
#                      <!DOCTYPE html>
#                      <html lang="en">
#                      <head>
#                          <meta charset="UTF-8">
#                          <title>Title</title>
#                      </head>
#                      <body>
#                      <h1>your score:%s</h1>
#
#                      </body>
#                      </html>
#                    ''' % count
#         func(*args)
#         return html
#     return inner

@gettime
# @score
def app(environ,start_response):
    print('environ:',environ)
    request_path = environ['path']
    print(request_path)
    if request_path=='/gettime.py':

        # 调用服务器的方法，拼接响应头部信息
        start_response('200 ok',[('server','wsgisever'),('name','guazi'),('request_path',request_path)])
        time_data = gettime()
        return time_data

    elif request_path == '/score.py':
        # 调用服务器的方法，拼接响应头部信息
        print(222222222222222222223000)
        start_response('200 ok', [('server', 'wsgisever'), ('name', 'guazi'), ('request_path', request_path)])
        # return 'hello world from WSGI'
        score_html = score()
        return score_html


    else:
        '''处理动态资源匹配不到的问题 404 '''
        start_response('404 NOT FOUND', [('server', 'wsgisever'), ('name', 'guazi'), ('request_path', request_path)])
        return '您请求的动态资源不存在'