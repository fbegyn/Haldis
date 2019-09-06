from flask import redirect, abort, session, url_for, render_template, Blueprint
from flask_login import LoginManager, current_user, logout_user

from app import app
from models import User
from zeus import zeus_login

import forms

from zeus import login_and_redirect_user, create_user

auth_bp = Blueprint("auth_bp", __name__)

login_manager = LoginManager()
login_manager.init_app(app)


def init_login(app):
    @app.login_manager.user_loader
    def load_user(userid):
        return User.query.filter_by(id=userid).first()


@app.route('/login', methods=['GET', 'POST'])
def login(login_form=None):
    # return zeus_login()
    login_form = forms.LoginForm()
    if login_form.validate_on_submit():
        username = login_form.username.data
        print(f'USERNAME: {username}')
        user = User.query.filter_by(username=username).first()
        if len(username) > 0 and user:
            return login_and_redirect_user(user)
        elif len(username) > 0:
            user = create_user(username)
            return login_and_redirect_user(user)
    return render_template('login.html', form=login_form)


@auth_bp.route("/logout")
def logout():
    if "zeus_token" in session:
        session.pop("zeus_token", None)
    logout_user()
    return redirect(url_for("general_bp.home"))


def before_request():
    if current_user.is_anonymous() or not current_user.is_allowed():
        abort(401)
