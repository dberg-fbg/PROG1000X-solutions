minuter = int(input("Hur många minuter ringer du på en månad?: "))
kostnad_per_minut = int(input("Ange kr/min: "))

kostnad = kostnad_per_minut * minuter

if kostnad >= 300:
    print(f"Du fick en rabbat och betalar: {kostnad * 0.9}")
else:
    print(f"Du fick ingen rabat och betalar: {kostnad}")

