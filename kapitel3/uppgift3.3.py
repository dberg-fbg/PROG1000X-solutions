points = int(input("Hur många poäng fick du på provet?: "))

print("Du fick betyget: ", end="")

# Bara en av grenarna kommer att köras.
# Python stannar därmed vid första sanna villkor.
if points >= 45:
    print("A")
elif points >= 40:
    print("B")
elif points >= 35:
    print("C")
elif points >= 30:
    print("D")
elif points >= 25:
    print("E")
else:
    print("F")
