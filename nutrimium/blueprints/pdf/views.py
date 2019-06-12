from flask import Blueprint, render_template, abort, make_response, request, session
from jinja2 import TemplateNotFound
import pdfkit
import json

from lib.meals import compute_number_of_days, compute_total_calories, compute_basket
from lib.recipes import RecipeService

meal_types = [
    ['Matin', 'Midi', 'Collation', 'Soir'],
    ['Matin', 'Midi', 'Collation', 'Soir'],
    ['Matin', 'Midi', 'Collation', 'Soir'],
    ['Matin', 'Midi', 'Collation', 'Soir'],
    ['Matin', 'Midi', 'Collation', 'Soir'],
    ['Matin', 'Midi', 'Collation', 'Soir'],
    ['Matin', 'Midi', 'Collation', 'Soir']
]


pdf = Blueprint('pdf', __name__,
                        template_folder='templates', url_prefix='/pdf')

@pdf.route('/')
def show():
    try:
        return 'hello world'
#        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        abort(404)



@pdf.route('/generate', methods=['POST'])
def generate():
    meal_plan = request.json

    session['meal_plan'] = meal_plan
    print(session.get('meal_plan'))

    print(meal_types[0][0])
    
    options = {
        'footer-html': 'http://localhost:5000/pdf/footer',
        'header-html': 'http://localhost:5000/pdf/header'
    }

    cover = 'http://localhost:5000/pdf/cover?number_of_days={0}&number_of_calories={1}'.format(
        compute_number_of_days(meal_plan),
        compute_total_calories(meal_plan)
    )

    urls = [
    'http://localhost:5000/pdf/basket/{0}'.format(json.dumps(meal_plan))
    ]


    for idx, day in enumerate(meal_plan):
        idx_day = idx + 1 ## 1-indexes for days (more human readable)
        print(idx_day)
        for idx_meal, recipe in enumerate(day):
            print(meal_types[idx][idx_meal])
            urls.append('http://localhost:5000/pdf/recipe/{0}/{1}/{2}/{3}'.format(recipe['name'], recipe['calories'], idx_day, meal_types[idx][idx_meal] ))


    print (urls)
            
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


@pdf.route('/basket/<meal_plan>')
def basket(meal_plan):

    meal_plan = json.loads(meal_plan)
    print("MEAL PLAN: {}".format(meal_plan))

    assert meal_plan is not None
    
    basket = compute_basket(meal_plan)
    print (basket)

    return render_template('basket.html', basket=basket)
