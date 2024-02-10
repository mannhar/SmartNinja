""" eine Funktion wird mit def name (): eingleitet
und im Code mit dem namen ausgeführt """


def multiprint():
    print("Hallo Welt")
    print("Hallo Harald")


multiprint()

""" in der Klammer können Parameter  übergeben werden """


def multiprint2(name):
    print(name)
    print(name)


multiprint2("hallo")

""" Es können Parameter wie namen, oder auch wie oft soll der Name ausgegeben werden
hier wird der Parameter name 5 mal ausgegeben"""


def multiprint3(name, count):
    for i in range(0, count):
        print(name)


multiprint3("Hallo", 5)


""" eine Funktion kann auch etwas retour geben, das die meisten Funktionen auch machen """

def weitere_funktionen(a, b):
    if a < b:
        return b
    else:
        return a

result = weitere_funktionen(3,7)
print(result)


""" es können auch Strings getrennt werden, es wird beim "|" getrennt """

print("Hallo|Welt".split("|"))

""" Ausgabe: ['Hallom', 'Welt'] """