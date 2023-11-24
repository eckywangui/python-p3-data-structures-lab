spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return[food['name'] for food in spicy_foods]
    pass

def get_spiciest_foods(spicy_foods):
    
     return[food['name']for food in spicy_foods if ["heat_level"] in spicy_foods >5]
     pass

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level_emojis = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}")
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    matching_foods = [food for food in spicy_foods if food["cuisine"] == cuisine]
    return matching_foods[0] if matching_foods else None
    pass

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food['heat_level'] > 5:
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}.")


    print_spiciest_foods(spicy_foods)
    pass

def get_average_heat_level(spicy_foods):
    total_heat = sum(food['heat_level'] for food in spicy_foods)
    num_foods = len(spicy_foods)

    if num_foods == 0:
        return 0

    average_heat = total_heat / num_foods
    
    average_heat = get_average_heat_level(spicy_foods)
    print(average_heat)
    
    pass

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    
    new_spicy_food = {"name": "Spicy Ramen", "cuisine": "Japanese", "heat_level": 7}

    updated_spicy_foods = create_spicy_food(spicy_foods, new_spicy_food)
    
    print(updated_spicy_foods)
    pass
