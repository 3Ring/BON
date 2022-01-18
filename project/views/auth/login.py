from flask import render_template, redirect, url_for
from flask_login import login_user
from flask_login import current_user

from project.models import Users
from project.forms.login import Login


def login_get():
    """if user isn't logged in direct them to login page.
    If the user is already logged in they will be directed to the index
    """
    if current_user.is_active:
        return redirect(url_for("main.index"))
    form = Login()
    return render_template("login.html", form=form)


def login_post():
    """checks data and logs in user if correct
    redirects user to index if they are already logged in
    """
    form = Login()
    if not form.validate_on_submit():
        return render_template("login.html", form=form)

    user = Users.query.filter_by(email=form.email.data).first()
    
    login_user(user, remember=form.remember.data)
    return redirect(url_for("main.index"))

