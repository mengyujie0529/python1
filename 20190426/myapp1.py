urlfuncdict = {}
def route(url):
    def wapper(func):
        urlfuncdict[url] = func
        def inner():
            responsebody = func()
            return responsebody
        return inner
    return wapper
@route("/login.py")
def login():
    print("login")
    return "login 页面"

def app(e,start_response):
    print('environ',e)
    path = e['path']
    print(path)
    try:
        start_response('200 ok',[('server','wsgi'),('name','za')])
        body = urlfuncdict[path]()
        return body
    except:
        start_response('404 not found', [('server', 'wsgi'), ('name', 'za')])
        return "找不到"