for i in range(0, 10):
    if i == 3:
        continue
    print(i)

""" 0 1 2 4 5 6 7 8 9 wird ausgegeben, aber die 3 , weil if i == 3 erreicht wurde und mit continue wird i 
wieder ausgegeben """

for i in range(0, 10):
    if i == 3:
        break
    print(i)
""" 0 1 2 wird ausgegeben und nach dem i == 3 """

liste = [2, 3, 5, 6, 7, 8, 9, 14, 23,]
""" es werden alle zahlen addiert' 
0 2 5 10 16 23 31 40 54 77 """
s = 0

for element in liste:
    s = s + element
print(s)


""" soll nur bis 10 zählen und dann aufhören"""
s = 0
for element in liste:
    s = s + element
    if s == 10:
        break
print(s)