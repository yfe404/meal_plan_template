from flask import Blueprint, render_template, abort, make_response, request
from jinja2 import TemplateNotFound
import pdfkit

from lib.meals import compute_number_of_days, compute_total_calories
from lib.recipes import RecipeService


data2 =  [[

{"calories": 400,
"proteins": 24,
"carbohydrates": 58,
"fats": 8,
"ingredients": [
{"name": "Fromage blanc 0%", "quantity": 150, "unit": "g"},
{"name": "Mangue", "quantity": 30, "unit": "g"},
{"name": "Myrtilles", "quantity": 50, "unit": "g"},
{"name": "Banane", "quantity": 50, "unit": "g"},
{"name": "Framboises", "quantity": 50, "unit": "g"},
{"name": "Muesli (sans sucre ajouté)", "quantity": 40, "unit": "g"},
{"name": "Oeuf(s) entier(s)", "quantity": 1, "unit": "unit"},
],             
"name": "Fromage blanc fruité", "steps": [
"Dans un grand bol: versez le fromage blanc et ajoutez les myrtilles et les framboises.",
"Coupez la mangue en dés et ajoutez les morceaux au fromage blanc.",
"Coupez la banane en tranches et ajoutez les morceaux au fromage blanc.",
"Ajoutez le muesli et mélangez.",
"Préparez les oeufs à part selon vos préférences, au plat, en omelette ou autre."
], "type": ["breakfast", "snack"]},



{"calories": 450,
"proteins": 41,
"carbohydrates": 29,
"fats": 19,
"ingredients": [
{"name": "Oeuf(s) entier(s)", "quantity": 3, "unit": "unit"},
{"name": "Blanc de poulet", "quantity": 80, "unit": "g"},
{"name": "Poivron", "quantity": 80, "unit": "g"},
{"name": "Champignons de Paris", "quantity": 80, "unit": "g"},
{"name": "Riz complet", "quantity": 35, "unit": "g"},
],
"name": "Omelette", "steps": [
"Dans un grand recipient: fouettez le oeufs. Vous pouvez ajouter du poivre et des épices selon vos préferences.",
"Dans un plat, coupez le blanc de poulet et les poivrons en dés.",
"Versez dans une poêle chaude votre mélange d'oeufs fouettés.",
"Ajoutez-y le poulet et les poivrons.",
"Laissez cuire jusqu'à ce que l'omelette soit prête.",
"Pour la cuisson du riz, référez-vous aux instructions présentes sur l'emballage (typiquement environ 10min dans une casserole d'eau bouillante)."
], "type": ['lunch', 'dinner']
},


{"calories": 500,
"proteins": 37,
"carbohydrates": 23,
"fats": 30,
"ingredients": [
{"name": "Fromage blanc 0%", "quantity": 100, "unit": "g"},
{"name": "Beurre de cacahuètes", "quantity": 20, "unit": "g"},
{"name": "Myrtilles", "quantity": 30, "unit": "g"},
{"name": "Framboises", "quantity": 30, "unit": "g"},
{"name": "Pomme", "quantity": 30, "unit": "g"},
{"name": "Graines de courge", "quantity": 20, "unit": "g"},
{"name": "Flocons de soja", "quantity": 50, "unit": "g"},
],
"name": "Fromage blanc fruité 2", "steps":[
"Dans un grand bol: versez le fromage blanc et le beurre de cacahuètes puis mélangez jusqu'à l'obtention d'un mélange homogène.",
"Ajoutez les myrtilles et les framboises.",
"Coupez la pomme en dés et ajoutez les morceaux au fromage blanc.",
"Ajoutez les flocons de soja et mélangez.",
"Ajoutez les graines de courge."
], "type": ["breakfast", "snack"]},



{"calories": 450,
"proteins": 26,
"carbohydrates": 27,
"fats": 25,
"ingredients": [
{"name": "Carottes râpées", "quantity": 70, "unit": "g"},
{"name": "Concombre", "quantity": 50, "unit": "g"},
{"name": "Feta", "quantity": 15, "unit": "g"},
{"name": "Noix", "quantity": 10, "unit": "g"},
{"name": "Blanc de poulet", "quantity": 80, "unit": "g"},
{"name": "Tomates", "quantity": 100, "unit": "g"},
{"name": "Jeunes pousses", "quantity": 40, "unit": "g"},
{"name": "Pois chiches (en boite)", "quantity": 60, "unit": "g"},
{"name": "Huile d'olive", "quantity": 1, "unit": "càs"},
{"name": "Vinaigre balsamique", "quantity": 1, "unit": "càs"},
],
"name": "Salade fraîche", "steps": [
"Dans un plat: râpez les carottes.",
"Coupez les tomates en morceaux.",
"Epluchez les concombres et coupez les en dés grossiers.",
"Emiettez la feta.",
"Concassez les noix.",
"Préchauffez votre poêle.",
"Coupez le poulet en morceaux.",
"Quand la poêle est suffisament chaude, ajoutez les morceaux de poulet.",
"Quand le poulet est cuit, vous pouvez l'ajouter à votre salade."
"Ajouter les pois chiches et les jeunes pousses.",
"Dans un petit recipient mélangez l'huile d'olive et le vinaigre balsamique. Vous pouvez ajouter du citron.",
"Assaisonner avec le mélange. Vous pouvez ajouter des épices et du poivre selon vos envies.",
"Mélangez le tout avec une grosse cuillère."
], "type": ["lunch", "dinner"]}
    
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
    
    basket = [dict(), dict()] # 2 pages
    pos = 0 # evenly spread the ingredients on the 2 pages 
    for meals_for_day in meal_plan:
        for recipe in meals_for_day:
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
