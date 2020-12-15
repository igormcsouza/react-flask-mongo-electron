from flask import Flask, jsonify

def create_app_minimal():
    
    app = Flask(__name__)

    return app

def create_app():

    app = create_app_minimal()

    @app.route('/health')
    def health():
        return jsonify({ "status": "ok" })

    return app