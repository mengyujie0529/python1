old_f=open("wb","rb")
new_f=open("wbcopy","wb")
list_obj=old_f.readlines()

#print(list_obj)

for obj in list_obj:
    new_f.write(obj)

old_f.close()
new_f.close()