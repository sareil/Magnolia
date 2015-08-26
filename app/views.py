from flask import render_template
from app import app
from .forms import LoginForm

# views
@app.route('/')
@app.route('/main')
def main():
    return render_template("main.html",
    title = 'Home')

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    return render_template('login.html',
    title = 'Login',
    form = form)

# error page
@app.errorhandler(404)
def internal_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500
