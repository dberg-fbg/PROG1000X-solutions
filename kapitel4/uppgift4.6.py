n = int(input("n? "))
summa = 0
for k in range(1, n + 1):
    summa = summa + k ** 2 # eller + k * k
print("Summan blir", summa)
