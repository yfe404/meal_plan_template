from flask import Blueprint, render_template, abort, make_response, request
from jinja2 import TemplateNotFound
import pdfkit

from lib.meals import compute_number_of_days, compute_total_calories
from lib.recipes import RecipeService


data2 =  [[
    {
        "calories": 400,
        "name": "Fromage blanc fruité"
    },
    {
        "calories": 450,
        "name": "Omelette"
    },
    {
        "calories": 500,
        "name": "Fromage blanc fruité 2"
    },
    {
        "calories": 450,
        "name": "Salade fraîche"
    }    
]]
    

meal_types = ['Matin', 'Midi', 'Collation', 'Soir']


pdf = Blueprint('pdf', __name__,
                        template_folder='templates', url_prefix='/pdf')

@pdf.route('/')
def show():
    try:
        return 'hello world'
#        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        abort(404)



@pdf.route('/generate')
def generate():

    options = {
        'footer-html': 'http://localhost:5000/pdf/footer',
        'header-html': 'http://localhost:5000/pdf/header'
    }

    cover = 'http://localhost:5000/pdf/cover?number_of_days={0}&number_of_calories={1}'.format(
        compute_number_of_days(data2),
        compute_total_calories(data2)
    )

    urls = [
        'http://localhost:5000/pdf/basket'
    ]

    for idx, day in enumerate(data2):
        idx_day = idx + 1 ## 1-indexes for days (more human readable)
        for idx_meal, recipe in enumerate(day):
            urls.append('http://localhost:5000/pdf/recipe/{0}/{1}/{2}/{3}'.format(recipe['name'], recipe['calories'], idx_day, meal_types[idx_meal] ))

    pdf = pdfkit.from_url(urls, False, options=options, cover=cover)

    response = make_response(pdf) 
    
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline' ## open the pdf in the browser VS attachement try to dl it.
    
    return response

@pdf.route('/cover')
def cover():
    n_days = request.args.get('number_of_days', '')
    n_calories = request.args.get('number_of_calories', '')
    return render_template('cover.html', number_of_days=n_days, number_of_calories=n_calories)

@pdf.route('/footer')
def footer():
    return render_template('footer.html')

@pdf.route('/header')
def header():
    return render_template('header.html')


@pdf.route('/recipe/<name>/<calories>/<day>/<meal_type>')
def recipe(name, calories, day, meal_type):
    recipe_service = RecipeService()
    recipe = recipe_service.get_recipe(name=name, calories=calories)
    
    if recipe is None:
        abort(404)

    return render_template('recipe.html', data=recipe, day=day, meal_type=meal_type)


@pdf.route('/basket')
def basket():
    meal_plan = data2
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

    print (basket)

    return render_template('basket.html', basket=basket)
