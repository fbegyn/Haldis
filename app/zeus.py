from flask import current_app, flash, redirect, request, session, url_for, Blueprint
from flask_login import login_user

from models import User, db

oauth_bp = Blueprint("oauth_bp", __name__)


def zeus_login():
    return current_app.zeus.authorize(
        callback=url_for("oauth_bp.authorized", _external=True)
    )


def login_and_redirect_user(user):
    login_user(user)
    return redirect(url_for("general_bp.home"))


def create_user(username):
    user = User()
    user.configure(username, False, 1)
    db.session.add(user)
    db.session.commit()
    return user
