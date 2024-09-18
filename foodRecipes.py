foodRecipesDict = {
    "Spaghetti": "Boil water, cook pasta, add sauce",
    "Tacos": "Prepare meat, add toppings, fill tortillas",
    "Pizza": "Prepare dough, add sauce, toppings, and bake",
    "Salad": "Chop vegetables, add dressing",
    "Pancakes": "Mix batter, cook on griddle",
    "Soup": "Boil broth, add vegetables and spices",
    "Omelette": "Whisk eggs, cook in pan, add fillings",
    "Brownies": "Mix ingredients, bake in oven"
}
print()
print(foodRecipesDict)
print()
print("Recipe of Pancakes:", foodRecipesDict["Pancakes"])
print()
foodRecipesDict["Pizza"] = "Prepare dough, add sauce, cheese, and bake"
print()
del foodRecipesDict["Omelette"]
print()
last_key = list(foodRecipesDict.keys())[-1]
print("Last key-value pair:", last_key, ":", foodRecipesDict[last_key])
print()
print()