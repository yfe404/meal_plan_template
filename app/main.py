from flask import Flask, render_template, make_response
import pdfkit

app = Flask(__name__)


@app.route('/')
def index():
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
                      
                    

