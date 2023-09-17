from market import app
from flask import render_template
from market.models import Item
from market.forms import RegisterForm

@app.route('/')
@app.route('/home')
def home_page():
  return render_template('home.html')

@app.route('/market')
def market_page():
  items = Item.query.all()
  return render_template('market.html', items=items)

@app.route('/register')
def register_page():
  form = RegisterForm()
  return render_template('register.html', form=form)

# Possible easter egg
# @app.route('/about/<username>')
# def about_page(username):
#   # return '<h1>Smurf Cat</h1><img src=https://i.kym-cdn.com/photos/images/newsfeed/002/652/460/d70.jpg height=440px width=440px alt=Smurf Cat/>\n<a href=http://127.0.0.1:5000/>Hello World</a>'

#   return f"<h1>This is the about page of {username}</h1>"