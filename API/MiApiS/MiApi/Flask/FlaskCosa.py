from flask import *

app = Flask(__name__)

countries = [
    {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408}
]

@app.get('/countries')
def get_all_countries():
    return jsonify(countries)

@app.route('/')
@app.get("/countries/<int:id>")
def get_countries(id):
    for country in countries:
        if country['id'] == id:
            return country, 200
    return {"error": "country not found"}, 404


def _find_next_id():
    return max(country["id"] for country in countries)+1

@app.post("/countries")
def add_country():
    if request.is_json:
        country = request.get_json()
        country["id"] = _find_next_id()
        countries.append(country)
        return country, 201
    return {"error": "Request must be JSON"}, 415

if __name__ == '__main__':
   app.run(debug=True, host = '0.0.0.0', port = 5050)