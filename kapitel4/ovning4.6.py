summa = 0
k = 1
while True:
    term = 1 / k
    if term < 0.001: 
        break

    if k % 2 == 0:
        summa -= term
    else:
        summa += term
    print(f"{summa=:.05f}")
    k += 1

print(f"{summa:.05f}") # ln(2)

