
matare_nu = int(input("Mätarställning i dag? "))
matare_gammal = int(input("Mätarställning för ett år sedan? "))

antal_mil = matare_nu - matare_gammal

print(f"Antal körda mil: {antal_mil}")

liter_bensin = float(input("Antal liter bensin: "))
liter_per_mil = liter_bensin / antal_mil

print(f"Förbrukning per mil: {liter_per_mil}")

