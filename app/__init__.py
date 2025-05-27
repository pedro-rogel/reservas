from flask_sqlalchemy import SQLAlchemy
from flask import Flask, redirect
from config import Config

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    db.init_app(app)
    
    from .swagger import swagger_bp
    app.register_blueprint(swagger_bp)
    @app.route("/")
    def raiz():
        return redirect("doc", code=302)
        
    from .controller import reserva_bp
    app.register_blueprint(reserva_bp)
    
    return app