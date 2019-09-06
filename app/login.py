from flask import redirect, abort, url_for, render_template, Blueprint
from flask_login import LoginManager, current_user, logout_user, login_user

from forms import LoginForm
from models import User, db
from models.anonymous_user import AnonymousUser

auth_bp = Blueprint("auth_bp", __name__)


def init_login(app):
    login_manager = LoginManager()
    login_manager.init_app(app)

    login_manager.anonymous_user = AnonymousUser

    @app.login_manager.user_loader
    def load_user(userid):
        return User.query.filter_by(id=userid).first()


@auth_bp.route('/login', methods=['GET', 'POST'])
def login(login_form=None):
    login_form = LoginForm()
    if login_form.validate_on_submit():
        username = login_form.username.data
        user = User.query.filter_by(username=username).first()
        if len(username) > 0 and user:
            return login_and_redirect_user(user)
        elif len(username) > 0:
            user = create_user(username)
            return login_and_redirect_user(user)
    return render_template('login.html', form=login_form)


def login_and_redirect_user(user):
    login_user(user)
    return redirect(url_for("general_bp.home"))


@auth_bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("general_bp.home"))


def before_request():
    if current_user.is_anonymous() or not current_user.is_allowed():
        abort(401)


def create_user(username):
    user = User()
    user.configure(username, False, 1)
    db.session.add(user)
    db.session.commit()
    return user
