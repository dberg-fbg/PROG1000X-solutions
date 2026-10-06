
km_per_mile = 1.609
liter_per_gallon = 3.785
miles_per_gallon = float(input("Ange förbrukningen i miles/gallon: "))

liter_per_mil = liter_per_gallon * 10 / (miles_per_gallon * km_per_mile)

print(f"Förbrukningen är {liter_per_mil:.3f} liter/mil")
