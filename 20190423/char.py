import  chardet
string1 = 'sad'
s2 = string1.encode()
print(
    type(s2)
)
print(type(chardet.detect(s2)))