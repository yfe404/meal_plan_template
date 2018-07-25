from flask import Flask, render_template, make_response, request
from nutrimium.blueprints.pdf import pdf

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)

#    from yourapplication.model import db
#    db.init_app(app)

#    from yourapplication.views.admin import admin
#    from yourapplication.views.frontend import frontend

    app.register_blueprint(pdf)
#    app.register_blueprint(frontend)


    return app
                      
                    
