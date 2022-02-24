print(" --- Der Taschenrechner --- ")
print()
eingabe = input("Wähle eine Rechnungsart ,+,-,*,:, =")
zahl1 = float(input("Erste Zahl:"))
zahl2 = float(input("Erste Zahl:"))

if eingabe == "+":
    print(zahl1+zahl2)
elif eingabe == "-":
    print(zahl1-zahl2)
elif eingabe == "*":
    print(zahl1*zahl2)
elif eingabe == ":":
    print((zahl1/zahl2))
