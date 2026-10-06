import math

x_1 = int(input("Ange x_1: "))
x_2 = int(input("Ange x_2: "))
y_1 = int(input("Ange y_1: "))
y_2 = int(input("Ange y_2: "))

distance = math.sqrt((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2 )

print("Avståndet mellan punkterna är", distance)
