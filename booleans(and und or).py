age = 35

if age >= 30:
    if age <= 39:
        print("Die Person ist in ihren 30-ern")

if age >= 30 and age <= 39:                             # wenn 2 Bedingungen erfüllt seine sollen
        print("Die Person ist in ihren 30-ern")

age = 25                                                # mit or muss nur eine erfüllt sein, können aber beide sein
if age < 30 or age >= 40:
    print("Diese Person ist nicht in ihren 30-ern")

print(age < 30)                                         # es wird ein booleans ausgegeben, es ist keine Zahl oder string
                                                        # es wird ein true oder false ausgegeben
above_30 = age >= 30

print(above_30)

if True:                                                # kürzeste If abfrage
    print(" if abfrage wurde ausgeführt")

above_20 = age >= 20                                    # hier wird abgefragt ob true
print(above_20)

if above_20:                                            # if above_20:(above_20 is true)
    print("alter ist unter 20")

country = "us"
age = 20

if (country == "us" and age >= 21) or (country != "us" and age >= 18):  # beide bedienungen sind false
    print("diese person darf trinken")
