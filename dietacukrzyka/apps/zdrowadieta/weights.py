def main(calories, massFractions, client_info, meal_type):
    meal_type = int(meal_type)
    age = float(client_info[0])
    weight = float(client_info[1])
    height = float(client_info[2])
    gender = client_info[3]  # male/female

    caloric_demand = 9.99 * weight + 6.25 * height - 4.92 * age
    if gender == "male":
        caloric_demand += 5
    else:
        caloric_demand -= 161

    # caloric of subsequent meals as a fraction of the whole day
    CALORIC_PER_MEAL = [0.25, 0.10, 0.30, 0.15, 0.20]
    TYPES_OF_MEALS = ["sniadanie", "II sniadanie",
                      "obiad", "podwieczorek", "kolacja"]

    this_meal = "sniadanie"
    cx = 0

    # checking the type of meal
    for i in range(len(TYPES_OF_MEALS)):
        if this_meal == TYPES_OF_MEALS[i]:
            # calorific value of the whole meal
            cx = CALORIC_PER_MEAL[meal_type] * caloric_demand
    cal = calories  # calorific value of each ingredient
    mf = massFractions  # mass fraction of each ingredient
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

    denominator = float(denominator)
    if (denominator > 1):
        mealWeight = cx / denominator  # weight of the whole meal
    else:
        mealWeight = cx * denominator
    ingredientsWeights = list()  # weight of each ingredient
    for i in range(length):
        ingredientsWeights.append(float(mf[i])*mealWeight)

    return_object = []
    return_object.append(mealWeight)
    return_object.append(ingredientsWeights)
    return_object.append(cx)

    return return_object
