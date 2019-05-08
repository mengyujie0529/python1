
urlfuncdict ={}
def route(url):
    print(url)
    def wapper(func):
        #添加键值对
        urlfuncdict[url] = func
        def inner():
            response_body = func()
            return response_body
        return inner
    return wapper
@route("/login.py")
def login():
    print("login")
    return "这是登录界面"


def app(environ,start_response):
    print('environ:', environ)
    request_path = environ['path']
    print(request_path)

    try:
        start_response('200 ok', [('server', 'wsgisever'), ('name', 'guazi'), ('request_path', request_path)])

        reponse_body = urlfuncdict[request_path]()
        return reponse_body
    except:
        start_response('404 not', [('server', 'wsgisever'), ('name', 'guazi'), ('request_path', request_path)])
        return '找不到'