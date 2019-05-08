urldict = {}
def route(url):
    def wapper(func):
        urldict[url]=func
        def inner():
            body = func()
            return body
        return inner
    return wapper

@route("/login.py")
def login ():
    print("登录页")
    return "zheshi denglu yemian "
def app(e,start_response):
    print(e)
    path = e["path"]

    try:

        start_response('200 ok', [('server', 'wsgisever'), ('name', 'guazi'), ('request_path', request_path)])
        body = urldict[path]()
        return body
    except:
        start_response('404 not found', [('server', 'wsgisever'), ('name', 'guazi'), ('request_path', request_path)])
        return "错误"
