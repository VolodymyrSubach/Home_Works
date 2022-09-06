from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


def get_connection():
    conn = sqlite3.connect('example.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def home_page():
    return 'Music shop'


@app.route('/best_selling/<int:quantity_tracks>')
def best_selling(quantity_tracks):
    conn = get_connection()
    track = conn.execute('SELECT ii.TrackId, t.Name Name, t.Composer Composer, SUM(ii.UnitPrice)Sum, COUNT(ii.Quantity)Quantity '
                         'FROM invoice_items ii '
                         'JOIN tracks t ON t.TrackId = ii.TrackId '
                         'GROUP BY ii.TrackId '
                         'ORDER BY COUNT(ii.Quantity) DESC '
                         'LIMIT ? ', (quantity_tracks,)).fetchall()
    conn.close()
    return render_template('best_sellings.html', track=track)


app.run(debug=True, port=5050)
