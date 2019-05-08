try:
    f = open("a.txt",encoding="utf-8")
    try:
        ret=f.read()
        print(ret)
    finally:
        f.close()
        print("文件已关闭")
# except FileNotFoundError:
#     print("文件未找到")
# except UnicodeDecodeError:
#     print("编码错误")
except Exception as e:
    print(e)
