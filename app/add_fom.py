from models import Location, Product
from app import db


flammage = {
        "Bicky Burger": 0,
        "Currydog": 0,
        "Hamburger": 0,
        "Cheeseburger": 0,
        "French fries with sauce": 0,
        "French fries with stew": 0,
        "Curry sausage": 0,
        "Curry sausage special": 0,
        "Aiki": 0,
        "Croque monsieur": 0,
        "Panini": 0,
        "Maxicano Baguette": 0,
        "Pizza Speciale": 0,
        "Pizza Hawai": 0,
        "Pizza Mozarella": 0,
        "Pizza Bolognese": 0,
        "Koude schotel": 0,
        "Chocolate pastry": 0,
        "Croissant": 0,
        "Donut": 0,
        "Sausage roll": 0,
        "Bouelette": 0,
        }

def add():
    flam = Location()
    flam.configure("Flammage FoM catering", "De toog, waar anders", "")
    db.session.add(flam)
    for food, price in flammage.items():
        entry = Product()
        entry.configure(flam, food, price)
        db.session.add(entry)
