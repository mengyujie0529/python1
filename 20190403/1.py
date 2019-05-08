file = open("history.csv",'r')
r=file.read()
print(r)
listContinent=[]#用来储存洲
listCountry=[]#用来储存国家
listInvent=[]#用来储存发明
dict1={}
v=dict1.fromkeys(['奴隶社会'],[])

# count = 0
# for obj in r:
#     if obj == ',' :
#         count += 1
#         if count % 4 ==0:
#             count=1
#     # print(count)
#     if count == 1 and obj!=',':
#         #把第一个，后到第二个，前的字符添加到列表
#         listContinent.append(obj)
#     elif count == 2 and obj!=',':
#         listCountry.append(obj)
#     elif count == 3 and obj!='\n'and obj!=',':
#         listInvent.append(obj)
# print(listContinent)
# print(listCountry)
# print(listInvent)


