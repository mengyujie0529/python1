import time
def app(environ,statr_response):
    time1 = time.ctime()
    statr_response('200 ok',[('server','wsgiserver')])
    return  time1
