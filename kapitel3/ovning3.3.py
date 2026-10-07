import math
alpha = float(input("Ange vinkel alpha: "))
a = float(input("Ange sida a: "))
b = float(input("Ange sidb b: "))

c = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(alpha))

if a == b == c:
    print("Liksidig")
elif a == b or b == c or a == c: 
    print("Likbent")
else:
    print("Oliksidig")
