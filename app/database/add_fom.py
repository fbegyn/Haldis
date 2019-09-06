import itertools

from app import db
from models import Location, Product

warm_snacks = {
    "French fries with sauce": 0,
    "French fries with stew": 0,
    "Currydog": 0,
    "FoM Burger": 0,
    "FoM Burger Cheese": 0,
    "Prom deal (FoM burger with fries)": 0,
    "Prom deal Cheese": 0,
    "Bicky Burger": 0,
    "Bicky Cheese": 0,
    "Ribster Burger": 0,
    "Hamburger": 0,
    "Cheeseburger": 0,
    "Mexicano": 0,
    "Mexicano baguette": 0,
    "Mexicano baguette with veggies": 0,
    "Curry sausage": 0,
    "Curry sausage special": 0,
    "Boulette": 0
}
continues_available = {
    "Aiki": 0,
    "Croque monsieur": 0,
    "Panini": 0,
}
half_baguettes = {
    "Half baguette with cheese/ham": 0,
    "Half baguette with cheese + ham": 0,
    "Half baguette with cheese/ham with veggies": 0,
    "Half baguette with cheese + ham and veggies (known as smos baguette)": 0,
}
pizza_pasta = {
    "Pizza Speciale": 0,
    "Pizza Hawai": 0,
    "Pizza Mozarella": 0,
    "Pasta Bolognese": 0,
    "Pasta Ham & Cheese": 0
}
cold_dish = {
    "Cold dish (veggies, ham, potatos, fruit)": 0
}
breakfast = {
    "Chocolate pastry": 0,
    "Croissant": 0,
    "Donut": 0,
    "Sausage roll": 0,
}


def add():
    flam = Location()
    flam.configure("Flammage FoM catering", "De toog, waar anders", "",
                   "https://www.fom.be/contents/view/food-and-drink")
    db.session.add(flam)
    for food, price in union(warm_snacks, continues_available, half_baguettes, pizza_pasta, cold_dish,
                             breakfast).items():
        entry = Product()
        entry.configure(flam, food, price)
        db.session.add(entry)


def union(*dicts):
    """
    Union n dictionaries
    :param dicts:
    :return:
    """
    return dict(itertools.chain.from_iterable(dct.items() for dct in dicts))
