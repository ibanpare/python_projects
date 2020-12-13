"""
Create a recipe class with ingredients and a put them in a recipe manager program 
that organizes them into categories like desserts, main courses 
or by ingredients like chicken, beef, soups, pies etc.
"""
import pdb
recipes = []
categories = set()

class Recipe:
    def __init__(self, name, category, ingredients = []):
        self.name = name
        self.category = category
        self.ingredients = ingredients
    def add_ingredient(self):
    	while True:
    		new_ingredient = str(input("Enter the ingredient you want to add (press enter to stop adding): "))
    		if len(new_ingredient) == 0:
    			break
    		self.ingredients.append(new_ingredient)

def add_recipe():
	print("Let's add a recipe!")
	recipe_name = str(input("Please add a name: "))
	recipe_category = str(input("Please add the recipe category: "))
	categories.add(recipe_category)
	new_recipe = Recipe(recipe_name, recipe_category)
	print(f"New recipe named {recipe_name} added!")
	print("Time to add ingredients now, if you'd like.")
	new_recipe.add_ingredient()
	recipes.append(new_recipe)


def list_by_category():
	recipe_names = []
	print("Let's list your recipes for a category you choose from the list below.")
	print("These are the available categories.")
	print(categories)
	chosen_category = str(input("What's your pick? "))
	for recipe in recipes:
		if recipe.category == chosen_category:
			recipe_names.append(recipe.name)
	print("These are the recipes we've found.")
	print(recipe_names)

def list_by_ingredient():
	recipe_names = []
	print(recipe_names)
	print("Let's find all recipes with an ingredient you choose")
	print("These are the available ingredients.")
	available_ingredients = set()
	for recipe in recipes:
		for ingredient in recipe.ingredients:
			available_ingredients.add(ingredient)
	print(available_ingredients)
	chosen_ingredient = str(input("What's your pick? "))
	for recipe in recipes:
		if chosen_ingredient in recipe.ingredients:
			recipe_names.append(recipe.name)
	print("These are the recipes we've found.")
	print(recipe_names)


add_recipe()
add_recipe()

list_by_ingredient()
#pdb.set_trace()