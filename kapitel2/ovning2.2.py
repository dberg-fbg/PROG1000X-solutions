import math

r = float(input("Ange en radie: "))
volym = 4 * math.pi * r ** 3 / 3
area = 4 * math.pi * r ** 2

print(f"{volym=:.02f}, {area=:.02f}")


