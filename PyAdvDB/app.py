import json

from flask import Flask, request
from flask_cors import CORS

from model import distances
from model.search_dto import SearchDto
from service import document_service


app = Flask(__name__, static_url_path='', static_folder='static')
CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route("/api/distances", methods=['GET'])
def get_distances():
    return distances.get_distances_as_json()


@app.route("/api/search", methods=['POST'])
def search_for():
    j = json.loads(json.dumps(request.get_json()))
    search_dto = SearchDto(**j)
    return document_service.search_for(search_dto)


if __name__ == '__main__':
    app.run()
