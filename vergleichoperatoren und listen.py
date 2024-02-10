students = ["Max", "Monika", "Erich", "Franziska"]

print("Monika" in students)         # in operator frag die liste students ab ob Monika enthalten ist -> TRUE
print("Lorenz" in students)         # → False
print("erich" in students)          # → auch False, weil nicht alle Zeichen übereinstimmen


if "Erich" in students:
    print("Ja, Monika studiert !")
else:
    print("Nein, Monika studiert hier nicht")
if "Moritz" in students:
    print("Ja, Moritz studiert !")
else:
    print("Nein, Moritz studiert hier nicht")

satz = "JA, hier stduieren alle!"
if "!" in satz:                     # → der in operator funktioniert auch mit Strings
    print("Ja")
else:
    print("Nein")