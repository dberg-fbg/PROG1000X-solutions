
bredd = int(input("Ange bredd: "))
langd = int(input("Ange längd: "))
tjocklek = int(input("Ange tjocklek: "))

if langd <= 600 and tjocklek <= 100 and (bredd + langd + tjocklek) <= 900 \
        and langd >= 140 and bredd >= 90:
    print("Brevet har tillåtna dimensioner")
else:
    print("Brevet har inte tillåtna dimensioner")


