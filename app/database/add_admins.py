from app import db
from models import User


def add():
    francis = User()
    francis.configure("francis", True, 0)
    db.session.add(francis)
