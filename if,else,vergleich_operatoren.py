n = 50
print("n ist:", n, "\n")

if n < 42:                          # mit if kann eine verzweigung erzeugt werden if (ist) n kleiner als 42 dann print n
    print("n ist kleiner als 42")

m = 10

if m > 5:
    print("m ist kleiner als 5")
else:                               # sonst print ist nicht der ...
    print("ist nicht der Fall")


# vergleichsoperatoren:
# booleans:
print(6 < 5)                        # gibt ein False zurück
print(5 < 6)                        # gibt ein True zurück

if 5 < 6:
    print("5 ist kleiner als 6")

result = 5 < 6                      # es können auch variable abgefragt werden, ob eine variable true ist
if result:
    print("5 ist kleiner wie 6")

print(6 > 5)
print(5 > 6)

print("ist 5 gleich 5")              # vergleichen
print(5 == 5)

word = "hallo"
print("ist Hello gleich", word)
print(word != "hallo")
print(word != "Hello")

word = "hallo"
print("ist hallo gleich", word)
print(word == "hallo")
print(word == "Hello")

print(5 > 5)                        # bei nummerischen vergleich, ist 5 nicht gleich 5
print(5 >= 5)                       # ist kleiner gleich
