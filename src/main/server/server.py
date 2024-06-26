from flask import Flask
from src.main.routes.trips_routes import trips_routes_bp

app = Flask(__name__)

app.register_blueprint(trips_routes_bp)
