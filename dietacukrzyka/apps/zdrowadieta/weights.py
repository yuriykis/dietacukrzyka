def main(calories, massFractions, client_info, meal_type):
    meal_type = int(meal_type)
    age = float(client_info[0])
    weight = float(client_info[1])
    height = float(client_info[2])
    gender = client_info[3]  # male/female
    physical_activity = 0 # int(client_info[4])
    
    # physical_activity
    # 0 - bezruch, niska aktywność fizyczna
    # 1 - umiarkowana aktywność fizyczna (1 − 3 razy w tygodniu trening lub dużo chodzenia w ciągu dnia)
    # 2 - średnia aktywność (3 − 5 treningów w tygodniu)
    # 3 - bardzo aktywny tryb życia
    # 4 - bardzo aktywny tryb życia + praca fizyczna
   
    PAL = [1.2, 1.3, 1.5, 1.7, 1.9]
    caloric_demand = 0
    if gender == "male":
        caloric_demand = 13.7 * weight + 5.0 * height - 6.76 * age + 66.47
    else:
        caloric_demand = 9.567 * weight + 1.85 * height - 4.68 * age + 655.1

    caloric_demand *= 1.1 # efekt termiczny pożywienia

    for i in range(len(PAL)):
        if i == physical_activity:
            caloric_demand *= PAL[i]
            break
        
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
