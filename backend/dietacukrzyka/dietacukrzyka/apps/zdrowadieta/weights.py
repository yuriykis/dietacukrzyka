def main(argv1, argv2):
    print(argv1[1])
    age = 51
    height = 170
    weight = 85
    gender = "male"  # male/female

    caloric_demand = 9.99 * weight + 6.25 * height - 4.92 * age

    if gender == "male":
        caloric_demand += 5
    else:
        caloric_demand -= 161

    print("Caloric demand: " + str(caloric_demand))

    # caloric of subsequent meals as a fraction of the whole day
    CALORIC_PER_MEAL = [0.25, 0.10, 0.30, 0.15, 0.20]
    TYPES_OF_MEALS = ["sniadanie", "II sniadanie", "obiad", "podwieczorek", "kolacja"]

    this_meal = "sniadanie"
    cx = 0

    # checking the type of meal
    for i in range(len(TYPES_OF_MEALS)):
        if this_meal == TYPES_OF_MEALS[i]:
            cx = CALORIC_PER_MEAL[0] * caloric_demand  # calorific value of the whole meal

    print("CX: " + str(cx))

    cal = [410, 59, 100, 200]  # calorific value of each ingredient
    mf = [0.1, 0.5, 0.1, 0.3]  # mass fraction of each ingredient
    length = len(cal)
    length2 = len(mf)

    try:
        if length != length2:
            raise DataBaseException
    except DataBaseException:
        print("Lista z kalorycznoscia skladnikow i procentem masowym skladnikow sa roznej dlugosci!")

    denominator = 0
    for i in range(length):
        denominator += mf[i] * cal[i] / 100

    mx = cx / denominator  # weight of the whole meal
    mi = list()  # weight of each ingredient

    for i in range(length):
        mi.append(mf[i]*mx)

    print(mx)

    print(mi)

    print(cx)