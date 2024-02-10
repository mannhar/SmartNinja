# mit der While Schleife kann ein Bereich so lange wiederholte werden, solange eine Bedienung erfüllt ist

counter = 0

while counter < 10:
    print(counter)
    counter = counter + 1
    print("Hallo eingerückt")   # wird hallo eingerückt nach jeder Zeile eingefügt

print("Hallo")                  # wenn der print-befehl nicht eingerückt wird
                                # wird er nur am ende der Schleife eingefügt