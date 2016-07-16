"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from ShoppingList import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/create')
def create():
    """Renders the create page."""
    return render_template(
        'create.html',
        title='Create',
        year=datetime.now().year,
        message='Create a List'
    )

@app.route('/view')
def view():
    """Renders the view page."""
    return render_template(
        'view.html',
        title='View',
        year=datetime.now().year,
        message='View Shopping List.'
    )

@app.route('/learn')
def learn():
    """Renders the learn page."""
    return render_template(
        'learn.html',
        title='View',
        year=datetime.now().year,
        message='Improve Results.'
    )

@app.route('/settings')
def settings():
    """Renders the settings page."""
    return render_template(
        'settings.html',
        title='Settings',
        year=datetime.now().year,
        message='Settings'
    )

@app.route('/signin')
def signin():
    return render_template(
        'signin.html',
        title='Sign In',
        year=datetime.now().year,
        message='Sign In'
    )

@app.route('/signup')
def signup():
    return render_template(
        'signup.html',
        title='Sign In',
        year=datetime.now().year,
        message='Sign Up'
    )

@app.route('/signout')
def signout():
    return render_template(
        'signout.html',
        title='Sign Out',
        year=datetime.now().year,
        message='Sign Out'
    )