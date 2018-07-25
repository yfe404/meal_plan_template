def compute_total_calories(meal_plan):
    total = 0
    for meals_for_day in meal_plan:
        for recipe in meals_for_day:
            total += recipe['calories']

    return total
    
def compute_number_of_days(meal_plan):
    return len(meal_plan)
