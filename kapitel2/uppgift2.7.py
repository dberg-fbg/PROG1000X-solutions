import math 


r = float(input("Ange circkels radie: "))
area = math.pi * r ** 2
omkrets = math.pi * 2 * r

print(f"{area=:.03f} {omkrets=:0.3f}")
