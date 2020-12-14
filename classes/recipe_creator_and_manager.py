"""
Exercise requirements:

Create a recipe class with ingredients and a put them in a recipe manager program 
that organizes them into categories like desserts, main courses 
or by ingredients like chicken, beef, soups, pies etc.

"""
recipes = []
categories = set()

class Recipe:
    def __init__(self, name, category, ingredients = []):
        self.name = name
        self.category = category
        self.ingredients = ingredients

def add_recipe():
    print()
    print("Let's add a recipe!")
    recipe_name = str(input("Please add a name: "))
    recipe_category = str(input("Please add the recipe category: "))
    recipe_ingredients = []
    categories.add(recipe_category)
    print("Time to add ingredients now, if you'd like.")
    while True:
        new_ingredient = str(input("Enter the ingredient you want to add (press enter to stop adding): "))
        if len(new_ingredient) == 0:
            break
        recipe_ingredients.append(new_ingredient)

    recipes.append(Recipe(recipe_name, recipe_category, recipe_ingredients))
    print(f"New recipe named {recipe_name} added!")
    print()

def list_by_category():
    recipe_names = []
    print()
    print("Let's list your recipes for a category you choose from the list below.")
    print()
    print("These are the available categories.")
    print()
    print(categories)
    chosen_category = str(input("What's your pick? "))
    for recipe in recipes:
        if recipe.category == chosen_category:
            recipe_names.append(recipe.name)
    print()
    print("These are the recipes we've found.")
    print(recipe_names)

def list_by_ingredient():
    recipe_names = []
    print()
    print("Let's find all recipes with an ingredient you choose")
    print()
    print("These are the available ingredients.")
    print()
    available_ingredients = set()
    for recipe in recipes:
        for ingredient in recipe.ingredients:
            available_ingredients.add(ingredient)
    print(available_ingredients)
    chosen_ingredient = str(input("What's your pick? "))
    for recipe in recipes:
        if chosen_ingredient in recipe.ingredients:
            recipe_names.append(recipe.name)
    print()
    print("These are the recipes we've found.")
    print(recipe_names)
    print()

#program loop
while True:
    print("******")
    print("Welcome to our recipe creator and manager!")
    print("You have the following actions:")
    print("1 - Add a Recipe")
    print("2 - List Recipes by Category")
    print("3 - List Recipes by Ingredient")
    print("4 - Quit")
    print("******")
    user_choice = str(input("What's your choice? "))
    if user_choice == "1":
        add_recipe()
    elif user_choice == "2":
        list_by_category()
    elif user_choice == "3":
        list_by_ingredient()
    elif user_choice == "4":
        break
