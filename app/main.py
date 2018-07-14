from flask import Flask, render_template, make_response
import pdfkit

app = Flask(__name__)

data = {
    "calories": 500,
    "proteins": 42,
    "carbohydrates": 39,
    "fats": 19,
    "ingredients": [
        {"name": "Oeuf entier", "quantity": 3, "unit": "unit"},
        {"name": "Blanc de poulet", "quantity": 80, "unit": "g"},
        {"name": "Poivron", "quantity": 80, "unit": "g"},
        {"name": "Champignons de Paris", "quantity": 80, "unit": "g"},
        {"name": "Riz complet", "quantity": 50, "unit": "g"},
    ],
    "name": "Omelette", "steps": [
        "Dans un grand recipient: fouettez le oeufs. Vous pouvez ajouter du poivres et des épices selon vos préferences.",
        "Dans un plat, coupez le blanc de poulet et les poivrons en dés.",
        "Versez dans une poêle chaude votre mélange d'oeufs fouettés.",
        "Ajoutez-y le poulet et les poivrons.",
        "Laissez cuire jusqu'à ce que l'omelette soit prête.",
        "Pour la cuisson du riz, référez-vous aux instructions présentes sur l'emballage (typiquement environ 10min dans une casserole d'eau bouillante)."
    ], "type": ['lunch', 'dinner']
}


@app.route('/')
def index():

    options = {
        'footer-html': 'http://localhost:5000/footer',
        'header-html': 'http://localhost:5000/header'
    }

    rendered = render_template('pdf_template.html', data=data)
    pdf = pdfkit.from_string(rendered, False, options=options)

    response = make_response(pdf) 
    
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline' ## open the pdf in the browser VS attachement try to dl it.
    
    return response

@app.route('/footer')
def footer():
    return render_template('pdf_footer.html')

@app.route('/header')
def header():
    return render_template('pdf_header.html')


@app.route('/test')
def test():
    return render_template('pdf_template.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
                      
                    


    
