year = int(input("Ange ett årtal: "))
n = 26_000

for y in range(1, year - 2022 + 1):
    n *= (1.007) * (1 - 0.006)
    n += 25 # -300 + 300

print(f"Antal invånare år {year}: {n}")
