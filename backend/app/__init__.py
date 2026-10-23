
from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)

    CORS(app)

    @app.get("/")
    def home():
        return {
            "message": "GharKharcha API is running",
            "status": "success",
        }

    @app.get("/api/health")
    def health_check():
        return {
            "status": "healthy",
            "service": "GharKharcha Backend",
        }

    return app
