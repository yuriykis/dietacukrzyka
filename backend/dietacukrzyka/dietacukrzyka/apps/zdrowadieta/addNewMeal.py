def main(ingredients, weights, meal_type):
    sum = 0
    for w in weights:
        sum += w
    massFractions = []
    for i in range(len(weights)):
        massFractions.append(weights[i]/sum)
    print(massFractions)
    return_object = []
    return_object.append(massFractions)