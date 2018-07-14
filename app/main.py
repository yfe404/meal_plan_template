from flask import Flask, render_template, make_response
import pdfkit

app = Flask(__name__)


@app.route('/')
def index():

    data = {
        "calories": 500,
        "proteins": 42,
        "carbohydrates": 39,
        "fats": 19,
        "ingredients": [
            {"name": "Oeuf entier", "quantity": 3, "unit": "g"},
            {"name": "Blanc de poulet", "quantity": 80, "unit": "g"},
            {"name": "Poivron", "quantity": 80, "unit": "g"},
            {"name": "Champignons de Paris", "quantity": 80, "unit": "g"},
            {"name": "Riz complet", "quantity": 50, "unit": "g"},
        ],
        "name": "Omelette", "steps": ["<RECIPE_STEPS>"], "type": ['lunch', 'dinner']
    }
    
    rendered = render_template('pdf_template.html')
    pdf = pdfkit.from_string(rendered, False)

    response = make_response(pdf) 
    
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline' ## open the pdf in the browser VS attachement try to dl it.
    
    return response


@app.route('/test')
def test():
    return render_template('pdf_template.html')


if __name__ == '__main__':
    app.run(debug=True)
                      
                    


    
