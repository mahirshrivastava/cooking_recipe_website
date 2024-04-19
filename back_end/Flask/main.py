"""Launch App File"""
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from urls.urls import add_urls

app = Flask(__name__)
CORS(app)
api = Api(app)
add_urls(api)

if __name__ == "__main__":
    app.run()