l = [0, 10, 20, 30, 40, 50]
def insert(num):
    count = 0#用来计数
    while num > l[count]:#如果插入的num>l中的数字，就把count加1
        count += 1
    l.insert(count,num)

if __name__ == '__main__':
    insert(25)
    insert(45)
    print(l)
