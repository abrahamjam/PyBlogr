from flask import Blueprint, render_template, redirect, url_for, flash, request
from .models import db, User
from flask_login import login_user, logout_user, login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def landing():
    return render_template('landing.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('main.index'))
        flash('Invalid username or password')
    return render_template('login.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User(username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful')
        return redirect(url_for('main.login'))
    return render_template('register.html')

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)
