hpy = "happy"
nrv = "nervous"
sd = "sad"

print("Willkommen zum 'Moodchecker'   -- Ver.0.1--")
print()
print("Choose: happy / nervous / sad ")

mood = input("Whats your mood : ")

if mood == hpy:
    print("It is great to see you happy!")
elif mood == nrv:
    print("Take a deep breath 3 times.")
    print("Take a deep breath 3 times.")
    print("...")
elif mood == sd:
    print("Let's go for a walk")
else:
    print("I don't feel it")
