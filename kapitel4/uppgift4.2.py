n = int(input("n? "))
summa = 0
k = 1
while k <= n:
    summa = summa + k ** 2 # eller + k * k
    k = k + 1
print("Summan blir", summa)
