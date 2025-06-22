from flask import Flask
from flask_cors import CORS
from .inv_routes import inventory_bp

def create_app():
    app = Flask(__name__)
    CORS(app)
    # CORS(app, resources={r"/api/*": {"origins": "*"}})

    app.register_blueprint(inventory_bp)

    return app