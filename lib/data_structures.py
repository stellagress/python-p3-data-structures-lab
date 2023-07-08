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
    return [food ["name"] for food in spicy_foods]



def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

 


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(food["name"], "(" + food["cuisine"] + ")", "|" , "Heat Level:" ,"🌶" * food["heat_level"])



def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food


# def get_spicy_food_by_cuisine(spicy_foods, cuisine):
#     for food in spicy_foods:
#         if food["cuisine"] == cuisine:
#             return food
#     return None



# [item for item in my_dict.items()]
# # [('a', 1), ('b', 2), ('c', 3), ('d', 4)]





def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            print(food["name"], "(" + food["cuisine"] + ")" , "|" , "Heat Level:", food["heat_level"] * "🌶")





def get_average_heat_level(spicy_foods):
    # for food in spicy_foods:
        return sum(food["heat_level"] for food in spicy_foods) / len(spicy_foods)
    


# def get_average_heat_level(spicy_foods):
#     total_heat = sum(food["heat_level"] for food in spicy_foods)
#     average_heat = total_heat / len(spicy_foods)
#     return average_heat




def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods













