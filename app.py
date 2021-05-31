from flask import Flask, render_template, url_for, abort
import data

app = Flask(__name__)

@app.errorhandler(404)
def render_not_found(_):
    return 'Упс, страница не найдена:(', 404

@app.route('/')
def index():
    return render_template('index.html', title=data.title,
                           departures=data.departures,
                           subtitle=data.subtitle,
                           description=data.description,
                           tours=data.tours)


@app.route('/departure/<dep>')
def departure(dep):
    tours = dict(filter(lambda tour: tour[1]['departure'] == dep, data.tours.items()))
    price_min = float('inf')
    price_max = float('-inf')
    nights_min = float('inf')
    nights_max = float('-inf')
    for tour in tours.values():
        if tour['price'] > price_max:
            price_max = tour['price']
        if tour['price'] < price_min:
            price_min = tour['price']
        if tour['nights'] > nights_max:
            nights_max = tour['nights']
        if tour['nights'] < nights_min:
            nights_min = tour['nights']
    if tours:
        return render_template('departure.html', title=data.title,
                               departures=data.departures,
                               tours=tours,
                               dep=dep,
                               price_min=price_min,
                               price_max=price_max,
                               nights_min=nights_min,
                               nights_max=nights_max)
    abort(404)


@app.route('/tour/<int:id>')
def tour(id):
    if id in data.tours.keys():
        return render_template('tour.html', title=data.title,
                               departures=data.departures,
                               id=id,
                               tours=data.tours)
    abort(404)


if __name__ == '__main__':
    app.run(debug=True)