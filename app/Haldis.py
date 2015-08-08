from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap, StaticCDN
from flask.ext.sqlalchemy import SQLAlchemy

from config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)

Bootstrap(app)
app.extensions['bootstrap']['cdns']['bootstrap'] = StaticCDN()
db = SQLAlchemy(app)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/orders')
def orders():
    return render_template('orders.html')


@app.route('/stats')
def stats():
    return render_template('stats.html')


if __name__ == "__main__":
    app.run(debug=True)
