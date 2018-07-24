from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

pdf = Blueprint('pdf', __name__,
                        template_folder='templates', url_prefix='/pdf')

@pdf.route('/')
def show():
    try:
        return 'hello world'
#        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        abort(404)
