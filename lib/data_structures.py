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
    names = []
    for food in spicy_foods:
        names.append(food['name'])
    return names

spicy_foods = [
    {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
    {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3},
    {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6},
]

print(get_names(spicy_foods))

# _______________________________________________________________________________________________
def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food['heat_level'] > 5]

spicy_foods = [
    {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
    {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3},
    {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6},
]

print(get_spiciest_foods(spicy_foods))


# _______________________________________________________________________________________________
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level = '🌶' * food['heat_level'] 
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")


spicy_foods = [
    {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
    {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3},
    {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6},
]

print_spicy_foods(spicy_foods)


# _______________________________________________________________________________________________
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food
    return None  


spicy_foods = [
    {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
    {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3},
    {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6},
]

print(get_spicy_food_by_cuisine(spicy_foods, "American"))

print(get_spicy_food_by_cuisine(spicy_foods, "Thai"))

print(get_spicy_food_by_cuisine(spicy_foods, "Indian"))


# _______________________________________________________________________________________________
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food
    return None

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level = '🌶' * food['heat_level']
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")

def print_spiciest_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food['heat_level'] > 5]
    print_spicy_foods(spiciest_foods)

spicy_foods = [
    {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
    {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3},
    {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6},
]

print_spiciest_foods(spicy_foods)


# _______________________________________________________________________________________________
def get_average_heat_level(spicy_foods):
    if not spicy_foods:
        return 0
    
    total_heat = sum(food['heat_level'] for food in spicy_foods)
    average = total_heat / len(spicy_foods)
    return int(average)


spicy_foods = [
    {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
    {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3},
    {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6},
]

print(get_average_heat_level(spicy_foods))


# _______________________________________________________________________________________________
def create_spicy_food(spicy_foods, new_spicy_food):
    spicy_foods.append(new_spicy_food)
    return spicy_foods


spicy_foods = [
    {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
    {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3},
    {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6},
]

new_food = {
    'name': 'Griot',
    'cuisine': 'Haitian',
    'heat_level': 10,
}

updated_spicy_foods = create_spicy_food(spicy_foods, new_food)
print(updated_spicy_foods)
