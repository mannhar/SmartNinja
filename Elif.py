currency = "€"
# das Problem bei diesen if-else anweisungen ist, das der Code immer weiter nach
# rechts wandert und sehr unübersichtlich wird
if currency =="$":
    print("US-Dollar")
else:
    if currency =="Y":
        print("Japanischer Yen")
    else:
        if currency == "€":
            print("Euro")
        else:
            if currency == "B":
                print("Thai Baht")

# mit elif was eine mischung aus else und if ist kann der Code besser gelesen werden
                                        # gelesen wird der code:
if currency == "$":                     # steht in der currency ein "$" dann:
    print("US-Dollar")                  # print ...
elif currency == "Y":                   # sonst wenn in der Variable currency ein "Y" steht
    print("Japanischer Yen")            # print ...
elif currency == "€":
    print("Euro")
# es wird das else mit dem if zusammengeführt el-if
        # else:
            # if currency =="B":
               # print("Thai Baht")
# dadurch wird der code immer wieder an den Rand gesetzt
elif currency == "B":
    print("Thai Bath")
else:
    print("nichts gefunden")