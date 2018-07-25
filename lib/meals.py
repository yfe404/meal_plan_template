from .recipes import RecipeService

def compute_total_calories(meal_plan):
    totals = [0 for _ in meal_plan]
    for day_idx, meals_for_day in enumerate(meal_plan):
        for recipe in meals_for_day:
            totals[day_idx] += recipe['calories']

    # check that all day has the same amount of calories
    for total in totals:
        assert total == totals[0]

    return totals[0]
    
def compute_number_of_days(meal_plan):
    return len(meal_plan)


def compute_basket(meal_plan):
    recipe_service = RecipeService()
    
    basket = [dict(), dict()] # 2 pages
    pos = 0 # evenly spread the ingredients on the 2 pages 
    for meals_for_day in meal_plan:
        for recipe in meals_for_day:
            recipe = recipe_service.get_recipe(recipe['name'], recipe['calories'])
            for ingredient in recipe['ingredients']:
                ingredient_name = ingredient['name']
                ingredient_quantity = ingredient['quantity']
                ingredient_unit = ingredient['unit']
                if ingredient_name in basket[0].keys():
                    basket[0][ingredient_name][0] += ingredient_quantity
                    pos = 1
                elif ingredient_name in basket[1].keys():
                    basket[1][ingredient_name][0] += ingredient_quantity
                    pos = 0
                else:
                    basket[pos][ingredient_name] = [ingredient_quantity, ingredient_unit]

    return basket
