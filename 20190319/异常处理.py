try:
    a=int(input('被除数：'))
    b=int(input('除数：'))
    print(a/b)
    #当出现错误，则该语句后面的都不执行

except Exception as e:
    print(e)
#捕获指定的错误
# except (ZeroDivisionError,NameError):
#     print("你错了")
#
# else:
#     pass
# finally:#一般情况下用来关闭文件操作
#     pass