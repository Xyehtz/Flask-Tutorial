from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
  return render_template('home.html')

@app.route('/market')
def market_page():
  items = [
    {'id': 1, 'name': 'Phone', 'barcode': '89321299897', 'price': 500},
    {'id': 2, 'name': 'Laptop', 'barcode': '82648827492', 'price': 900},
    {'id': 3, 'name': 'Keyboard', 'barcodee': '74820847520', 'price': 150}
  ]
  return render_template('market.html', items=items)

# Possible easter egg
# @app.route('/about/<username>')
# def about_page(username):
#   # return '<h1>Smurf Cat</h1><img src=https://i.kym-cdn.com/photos/images/newsfeed/002/652/460/d70.jpg height=440px width=440px alt=Smurf Cat/>\n<a href=http://127.0.0.1:5000/>Hello World</a>'

#   return f"<h1>This is the about page of {username}</h1>"