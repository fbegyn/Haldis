from flask import render_template
from utils import get_current_year


def home():
    return render_template('home.html')


def orders():
    return render_template('orders.html')


def stats():
    return render_template('stats.html')


def route(app):
    app.add_url_rule('/', view_func=home)
    app.add_url_rule('/orders/', view_func=orders)
    app.add_url_rule('/stats/', view_func=stats)


def add_filters(app):
    @app.template_filter('year')
    def year(_):
        return get_current_year()
