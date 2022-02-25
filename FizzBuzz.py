zahl = int(input("Zahl eingeben:"))
print("Ihre Zahl :", zahl)

for zahl1 in range(1, zahl+1):
    if zahl1 % 3 ==0 and zahl1% 5 == 0:
        print("fizzbuzz")
    elif zahl1 % 5 == 0:
        print("buzz")
    elif zahl1 % 3 == 0:
        print("fizz")
    else:
        print(zahl1)


