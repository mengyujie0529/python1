urldict = {}

def route(url):
    def wapper(func):
        urldict[url] = func
        def inner():
            body = func()
            return body

        return inner
    return wapper
@route("/login.py")
def login():
    print("登录页面")
    return "这是登录页面"

def app(e,start_response):
    print(e)
    path = e['path']
    print(path)
    try:
        start_response('200 ok', [('server', 'wsgisever'), ('name', 'guazi'), ('request_path', request_path)])
        body = urldict[path]()
        return body
    except:
        print("错误")
