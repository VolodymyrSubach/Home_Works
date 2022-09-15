from application import app
from utils import utils
from webargs.flaskparser import use_kwargs
from webargs import fields
from flask import render_template


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/rates')
@use_kwargs(
    {'currency': fields.Str(required=True)},
    location='query')
def get_value(currency):
    json_data = utils.get_json()
    for i in json_data:
        if len(currency) == 3 and currency.isalpha() and i['code'] == currency.upper():
            value = i['rate']
            return render_template('rates.html', value=value, currency=currency)
