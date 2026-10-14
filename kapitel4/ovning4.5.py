while True:
    h = float(input("Ange en höjd: "))

    if h <= 0:
        break

    antal_studs = 0
    while h > 1:
        h *= 0.7 # h = h * 0.7
        antal_studs += 1

    print(f"Bollen studsade {antal_studs} gånger")
