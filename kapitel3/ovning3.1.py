minuter = int(input("Ange antalet minuter du ringer: "))
print("Du gynnas mest av abonnemanget: ", end="")

if minuter <= 33:
    print("Kontant")
elif 33 < minuter < 66:
    print("Normal")
else:
    print("Plus")
