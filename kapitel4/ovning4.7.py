while True:
    n_judges = int(input("Ange antalet domare: "))
    if n_judges < 0: break
    if n_judges < 3:
        print("Minst 3 domare behövs")
        continue

    jump_difficulty = int(input("Ange hoppets svårighetsgrad: "))
    if jump_difficulty < 0: break

    judging_points = 0

    smallest = 2**32 - 1
    largest = 0

    i = 0
    while i < n_judges:

        points = int(input(f"Ange poängen från domare{i + 1}: "))
        if points < 0: break
        if points > 10: 
            print("Domarpoängen behöver vara mellan 0 och 10")
            continue

        if points < smallest:
            smallest = points
        if points > largest:
            largest = points

        judging_points += points

        i += 1

    judging_points = judging_points - largest - smallest

    judging_mean = judging_points / (n_judges - 2)

    final_result = judging_mean * 3 * jump_difficulty

    print(final_result)
    print()


