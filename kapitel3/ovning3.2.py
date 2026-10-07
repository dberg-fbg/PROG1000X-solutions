import math 
r = float(input("Ange circkels radie: "))
if r > 0:
    area = math.pi * r ** 2
    omkrets = math.pi * 2 * r

    print(f"{area=:.03f} {omkrets=:0.3f}")
else: 
    print("Du måste ange en positiv radie")
